# Range-Scalp Bot

*Updated Tue Oct 27 13:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36580 | 31942 | 4638 (43) | 0 | $-10127.73 | -4.4% |
| **+10¢** | 27330 | 21967 | 5363 (65) | 0 | $-8934.56 | -5.2% |
| **+15¢** | 22865 | 17110 | 5755 (89) | 0 | $-7856.14 | -5.5% |
| **+20¢** | 20264 | 14236 | 6028 (113) | 0 | $-6867.85 | -5.4% |
| **+10¢ (15¢ stop)** | 44829 | 44766 | 63 (33) | 0 | $-17089.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 13:04 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 13:04 | +10 stop | XRP | DOWN | 0.55 | 0.69 | 1.07 |
| 10-27 13:04 | +10 | XRP | DOWN | 0.54 | 0.69 | 1.17 |
| 10-27 13:04 | +5 | ZEC | DOWN | 0.66 | 0.83 | 1.49 |
| 10-27 13:04 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-27 13:04 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 13:04 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-27 13:03 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 13:03 | +10 stop | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 13:03 | +20 | ETH | DOWN | 0.61 | 0.84 | 2.03 |
| 10-27 13:03 | +15 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 10-27 13:03 | +10 | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 13:03 | +5 | ETH | DOWN | 0.61 | 0.69 | 0.48 |
| 10-27 13:02 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.48 |
| 10-27 13:01 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 13:01 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-27 13:01 | +15 | XRP | DOWN | 0.59 | 0.76 | 1.40 |
| 10-27 13:01 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 13:01 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-27 13:01 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 13:01 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-27 13:01 | +15 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-27 13:01 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 13:01 | +5 | BTC | DOWN | 0.69 | 0.78 | 0.62 |
| 10-27 13:01 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-27 13:01 | +20 | SOL | DOWN | 0.63 | 0.84 | 1.83 |
| 10-27 13:01 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-27 13:01 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-27 13:01 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-27 13:01 | +10 stop | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 10-27 13:01 | +20 | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 10-27 13:01 | +15 | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 10-27 13:01 | +10 | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 10-27 13:01 | +5 | ZEC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-27 13:01 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-27 13:01 | +20 | NEAR | DOWN | 0.60 | 0.81 | 1.82 |
| 10-27 13:01 | +15 | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 10-27 13:01 | +10 | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-27 13:01 | +5 | NEAR | DOWN | 0.58 | 0.67 | 0.56 |
| 10-27 13:01 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
