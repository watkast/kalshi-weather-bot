# Range-Scalp Bot

*Updated Mon Nov 16 01:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61474 | 53645 | 7829 (115) | 0 | $-16527.38 | -4.3% |
| **+10¢** | 45916 | 36742 | 9174 (156) | 0 | $-15497.29 | -5.4% |
| **+15¢** | 38468 | 28570 | 9898 (195) | 0 | $-14140.84 | -5.9% |
| **+20¢** | 34289 | 23906 | 10383 (247) | 0 | $-12397.19 | -5.8% |
| **+10¢ (15¢ stop)** | 74803 | 74649 | 154 (90) | 0 | $-27487.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 01:07 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-16 01:07 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-16 01:07 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-16 01:07 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 11-16 01:07 | +10 stop | ZEC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-16 01:06 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-16 01:06 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.78 |
| 11-16 01:06 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-16 01:06 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-16 01:06 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-16 01:06 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.80 |
| 11-16 01:06 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 11-16 01:06 | +10 | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 01:06 | +5 | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 01:06 | +10 stop | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 01:06 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 01:06 | +10 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 01:06 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 11-16 01:06 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 01:06 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-16 01:06 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 01:06 | +5 | BTC | DOWN | 0.71 | 0.80 | 0.63 |
| 11-16 01:04 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-16 01:04 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-16 01:02 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 01:02 | +20 | XRP | DOWN | 0.71 | 0.93 | 1.99 |
| 11-16 01:02 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 11-16 01:02 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-16 01:02 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-16 01:02 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-16 01:02 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 11-16 01:02 | +15 | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 11-16 01:02 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 01:02 | +5 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 01:02 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 01:02 | +20 | SOL | DOWN | 0.66 | 0.92 | 2.42 |
| 11-16 01:02 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 01:02 | +10 | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 01:02 | +5 | SOL | DOWN | 0.66 | 0.73 | 0.40 |
| 11-16 01:01 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
