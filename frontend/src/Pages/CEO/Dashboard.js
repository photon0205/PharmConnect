import React, { useEffect, useState } from "react";
import {
  Button,
  Select,
  Box,
  Text,
  Card,
  CardBody,
  HStack,
  Divider,
} from "@chakra-ui/react";
import StatCard from "./Cards/StatCard";
import axios from "axios";
import ProductTable from "./ProductTable";

const CEODashboard = () => {
  const [stores, setStores] = useState([]);
  const [products, setProducts] = useState([]);
  useEffect(() => {
    // axios.get('http://localhost:5000/api/ceo/dashboard')
    //     .then((response) => {
    //         setStores(response.data.stores);
    //         setProducts(response.data.products);
    //     })

    setStores([
      {
        id: 1,
        name: "Store 1",
        location: "Location 1",
      },
      {
        id: 2,
        name: "Store 2",
        location: "Location 2",
      },
    ]);
  }, []);
  // return a box which uses chakra dropdown selection to select the store and display the products of that store
  // the products are displayed in a table with many columns use chakra table and chakra dropdown
  return (
    <div>
      <Card margin="20px">
        <CardBody>
          <Text fontSize="2xl"  marginBottom={'2vh'}> Select Store</Text>
          <Select defaultValue={stores[0]} style={{ height: "8vh" }}>
            {stores.map((store) => (
              <option key={store.id} value={store.id}>
                {store.name}
              </option>
            ))}
          </Select>
        </CardBody>
      </Card>
      <Card margin="20px">
        <CardBody>
          <Text fontSize="2xl">Overall Inventory</Text>
          {/* make this Hstack cover the remaining of the card properly like flex space between and also add line for divider */}
          {/* add a visible divider in the HStack which line is visible */}
          <HStack
            px={12}
            py={3}
            boxShadow="lg"
            pos="sticky"
            top={0}
            left={0}
            id="top-nav"
            zIndex="banner"
            bg="white"
            justifyContent="space-between"
            marginTop={'4vh'}
          >
            <StatCard
              heading={"Categories"}
              value1={14}
              value2={null}
              subhead={null}
              color={"#1570EF"}
            />
            <Divider orientation="vertical" />
            <StatCard
              heading={"Total Products"}
              value1={868}
              value2={"₹25000"}
              subhead={"Revenue"}
              color={"#E19133"}
            />
            <Divider orientation="vertical" />
            <StatCard
              heading={"Top Selling"}
              value1={5}
              value2={"₹2500"}
              subhead={"Cost"}
              color={"#845EBC"}
            />
            <Divider orientation="vertical" />
            <StatCard
              heading={"Low Stocks"}
              value1={12}
              value2={"2"}
              subhead={"Not in Stock"}
              color={"#F36960"}
            />
          </HStack>
        </CardBody>
      </Card>
      <Card margin="20px">
        <CardBody>
          <HStack justifyContent="space-between" marginBottom={'2vh'}>
            <Text fontSize="2xl">Products</Text>
            <Box display="flex" alignItems="center" marginRight="16vw">
              <Button colorScheme="blue" marginRight={"0.5vw"}>
                Add Product
              </Button>
              <Button
                colorScheme="gray"
                bg="white"
                borderColor="gray.400"
                borderWidth="2px"
                marginRight={"0.5vw"}
              >
                Button Text
              </Button>
              <Button
                colorScheme="gray"
                bg="white"
                borderColor="gray.400"
                borderWidth="2px"
              >
                Download all
              </Button>
            </Box>
          </HStack>
          <ProductTable />
        </CardBody>
      </Card>
    </div>
  );
};

export default CEODashboard;
