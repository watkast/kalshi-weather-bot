# Range-Scalp Bot

*Updated Sat Nov 07 15:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51142 | 44584 | 6558 (78) | 1 | $-14298.94 | -4.4% |
| **+10¢** | 38187 | 30542 | 7645 (105) | 1 | $-13277.34 | -5.5% |
| **+15¢** | 31964 | 23722 | 8242 (134) | 1 | $-12222.58 | -6.1% |
| **+20¢** | 28428 | 19789 | 8639 (177) | 3 | $-10791.86 | -6.1% |
| **+10¢ (15¢ stop)** | 62291 | 62188 | 103 (61) | 0 | $-23018.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 15:37 | +10 stop | ZEC | DOWN | 0.49 | 0.60 | 0.75 |
| 11-07 15:36 | +10 stop | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-07 15:36 | +20 | NEAR | DOWN | 0.64 | 0.86 | 1.94 |
| 11-07 15:36 | +15 | NEAR | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 15:36 | +10 | NEAR | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 15:36 | +5 | NEAR | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 15:36 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-07 15:35 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-07 15:35 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-07 15:33 | +10 stop | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 11-07 15:33 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-07 15:33 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-07 15:33 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 15:33 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 15:33 | +10 stop | ZEC | DOWN | 0.64 | 0.49 | -1.85 |
| 11-07 15:33 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-07 15:33 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-07 15:32 | +10 stop | ZEC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-07 15:32 | +20 | ZEC | DOWN | 0.55 | open |  |
| 11-07 15:32 | +15 | ZEC | DOWN | 0.55 | 0.72 | 1.37 |
| 11-07 15:32 | +10 | ZEC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-07 15:32 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.45 |
| 11-07 15:32 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 15:32 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-07 15:32 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 15:32 | +10 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 15:32 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 11-07 15:32 | +10 stop | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-07 15:32 | +20 | DOGE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-07 15:32 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-07 15:32 | +10 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-07 15:32 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-07 15:32 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.26 |
| 11-07 15:32 | +20 | BNB | DOWN | 0.64 | 0.90 | 2.43 |
| 11-07 15:32 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.26 |
| 11-07 15:32 | +10 | BNB | DOWN | 0.64 | 0.79 | 1.26 |
| 11-07 15:32 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.64 |
| 11-07 15:32 | +5 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-07 15:31 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 11-07 15:31 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
