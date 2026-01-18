import "dotenv/config";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const METABASE_URL = process.env.METABASE_URL;
const METABASE_API_KEY = process.env.METABASE_API_KEY;

async function metabaseUserCurrent() {
  if (!METABASE_URL) throw new Error("METABASE_URL is missing");
  if (!METABASE_API_KEY) throw new Error("METABASE_API_KEY is missing");

  const res = await fetch(`${METABASE_URL}/api/user/current`, {
    headers: {
      "X-API-KEY": METABASE_API_KEY,
      "Content-Type": "application/json"
    }
  });

  const text = await res.text();
  if (!res.ok) throw new Error(`Metabase error ${res.status}: ${text}`);

  return text; // return raw JSON text for now
}

const server = new Server(
  { name: "metabase-mcp-adapter", version: "0.1.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "metabase_ping",
        description: "Verify connection/auth to Metabase by calling /api/user/current",
        inputSchema: {
          type: "object",
          properties: {},
          additionalProperties: false
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "metabase_ping") {
    const result = await metabaseUserCurrent();
    return {
      content: [{ type: "text", text: `Metabase OK:\n${result}` }]
    };
  }

  return {
    content: [{ type: "text", text: `Unknown tool: ${request.params.name}` }]
  };
});

const transport = new StdioServerTransport();
await server.connect(transport);
