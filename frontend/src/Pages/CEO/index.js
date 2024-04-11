import React, { useState } from 'react';
import Navbar from '../../components/Navbar';
import WithSidebarWrapper from './WithSidebarWrapper';
import SideNavContent from './SideNavContent';
import ManageStore from './ManageStore';
import CEODashboard from './Dashboard';

const CEO = () => {
  const [stage, setStage] = useState(0);
  const renderStage = () => {
    switch (stage) {
      case 0:
        return (
          <CEODashboard />
        );
      case 1:
        return (
          <CEODashboard />
        );
      case 2:
        return (
          <ManageStore />
        );
      default:
        return null;
    }
  }
  return (
    <div>
      <Navbar />
      <WithSidebarWrapper sidebarContent={<SideNavContent stage={stage} setStage={setStage}/>}>{renderStage()}</WithSidebarWrapper>
    </div>
  );
}

export default CEO;