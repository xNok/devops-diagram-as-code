import type { TinaField } from "tinacms";
export function portfolioFields() {
  return [
    {
      type: "string",
      name: "title",
      label: "title",
    },
    {
      type: "image",
      name: "image",
      label: "image",
    },
    {
      type: "string",
      name: "client",
      label: "client",
    },
    {
      type: "string",
      name: "year",
      label: "year",
    },
    {
      type: "string",
      name: "description",
      label: "description",
    },
    {
      type: "string",
      name: "category",
      label: "category",
    },
    {
      type: "string",
      name: "project_url",
      label: "project_url",
    },
    {
      type: "string",
      name: "type",
      label: "type",
    },
  ] as TinaField[];
}
export function postFields() {
  return [
    {
      type: "string",
      name: "title",
      label: "title",
    },
    {
      type: "datetime",
      name: "date",
      label: "date",
    },
    {
      type: "image",
      name: "image",
      label: "image",
    },
    {
      type: "string",
      name: "description",
      label: "description",
    },
    {
      type: "string",
      name: "categories",
      label: "categories",
      list: true,
    },
    {
      type: "string",
      name: "tags",
      label: "tags",
      list: true,
    },
    {
      type: "string",
      name: "type",
      label: "type",
    },
  ] as TinaField[];
}
