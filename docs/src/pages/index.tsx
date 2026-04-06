import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs">
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="A sample Python library for testing PR docs review">
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              <div className={clsx('col col--4')}>
                <div className="text--center padding-horiz--md">
                  <Heading as="h3">Simple API</Heading>
                  <p>Intuitive interface for GET and POST requests with minimal boilerplate.</p>
                </div>
              </div>
              <div className={clsx('col col--4')}>
                <div className="text--center padding-horiz--md">
                  <Heading as="h3">Configurable</Heading>
                  <p>Set timeouts, base URLs, and other options to match your needs.</p>
                </div>
              </div>
              <div className={clsx('col col--4')}>
                <div className="text--center padding-horiz--md">
                  <Heading as="h3">Utilities Included</Heading>
                  <p>Response parsing and URL building helpers out of the box.</p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
