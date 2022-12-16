# docker-graphql-template
### graphiql UI
http://YOUR_SERVER:8000/graphql/

### curl
curl -XPOST 'http://YOUR_SERVER:8000/graphql/' -H 'Content-Type: application/json' -d '{"query":"{hello(name: \"GraphQL test\")}"}'
