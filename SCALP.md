# Range-Scalp Bot

*Updated Tue Oct 20 06:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25221 | 21955 | 3266 (31) | 1 | $-7411.75 | -4.7% |
| **+10¢** | 18976 | 15202 | 3774 (46) | 1 | $-6590.05 | -5.5% |
| **+15¢** | 15880 | 11815 | 4065 (70) | 2 | $-5944.12 | -6.0% |
| **+20¢** | 14035 | 9780 | 4255 (88) | 6 | $-5353.57 | -6.1% |
| **+10¢ (15¢ stop)** | 30935 | 30883 | 52 (30) | 1 | $-11499.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 06:08 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-20 06:07 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 10-20 06:06 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-20 06:06 | +10 | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-20 06:06 | +5 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-20 06:05 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 10-20 06:05 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-20 06:04 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-20 06:04 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-20 06:04 | +15 | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 10-20 06:04 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-20 06:04 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-20 06:04 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-20 06:04 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 06:04 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-20 06:04 | +10 stop | BNB | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 06:04 | +15 | BNB | DOWN | 0.58 | 0.76 | 1.49 |
| 10-20 06:04 | +10 | BNB | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 06:04 | +5 | BNB | DOWN | 0.59 | 0.65 | 0.27 |
| 10-20 06:04 | +10 stop | NEAR | DOWN | 0.69 | 0.54 | -1.83 |
| 10-20 06:04 | +10 stop | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-20 06:04 | +10 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-20 06:04 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-20 06:04 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 06:04 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-20 06:04 | +15 | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 06:04 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 06:04 | +5 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-20 06:04 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.43 |
| 10-20 06:02 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 06:02 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-20 06:02 | +15 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 10-20 06:02 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 06:02 | +5 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 06:02 | +10 stop | NEAR | DOWN | 0.71 | 0.56 | -1.83 |
| 10-20 06:02 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 10-20 06:02 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 06:02 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.84 |
| 10-20 06:02 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-20 06:02 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
