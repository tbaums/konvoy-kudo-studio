FROM node:12-alpine

# install dependencies
WORKDIR /app
# COPY package.json package-lock.json ./
COPY . .
# RUN npm ci --production
# RUN npm run build
RUN npm install npx
RUN npx sapper export

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
# FROM node:12-alpine

# WORKDIR /app
# COPY --from=0 /app .
# COPY . .


EXPOSE 3000
CMD ["npx serve", "__sapper__/export"]