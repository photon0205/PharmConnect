import { useState, useEffect } from "react";
import { Text, Card, CardBody, HStack, Box, Button } from "@chakra-ui/react";
import StoreCard from "./Cards/StoreCard";

const ManageStore = () => {
  const [stores, setStores] = useState([]);
  useEffect(() => {
    // fetch("http://localhost:5000/api/v1/stores")
    //   .then((res) => res.json())
    //   .then((data) => {
    //     setStores(data);
    // });
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
  return (
    <Card margin="20px">
      <CardBody>
        <HStack justifyContent="space-between" marginBottom={"2vh"}>
          <Text fontSize="2xl">Manage Stores</Text>
          <Box display="flex" alignItems="center" marginRight="2vw">
            <Button backgroundColor={'#034C9D'} color='white' width={'8vw'}>
              Add Store
            </Button>
          </Box>
        </HStack>
      </CardBody>
      <CardBody>
        {stores.map((store) => (
          <StoreCard key={store.id} store={store} />
        ))}
      </CardBody>
    </Card>
  );
};

export default ManageStore;
