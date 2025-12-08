FROM node:20

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN pnpm install

COPY . .
RUN pnpm build

EXPOSE 5173

ENV PORT=5173
ENV HOST=0.0.0.0
CMD ["node", "build"]