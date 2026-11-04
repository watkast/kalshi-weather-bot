# Range-Scalp Bot

*Updated Wed Nov 04 20:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47463 | 41325 | 6138 (73) | 0 | $-13706.20 | -4.6% |
| **+10¢** | 35459 | 28339 | 7120 (98) | 0 | $-12535.86 | -5.6% |
| **+15¢** | 29698 | 22032 | 7666 (126) | 0 | $-11492.50 | -6.2% |
| **+20¢** | 26389 | 18360 | 8029 (166) | 0 | $-10145.93 | -6.1% |
| **+10¢ (15¢ stop)** | 57849 | 57756 | 93 (56) | 0 | $-21550.57 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 19:48 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-04 19:48 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.88 |
| 11-04 19:48 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-04 19:48 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-04 19:48 | +5 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-04 19:48 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-04 19:47 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-04 19:47 | +20 | DOGE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-04 19:47 | +15 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 11-04 19:47 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 19:47 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 19:47 | +10 stop | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-04 19:47 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-04 19:47 | +15 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-04 19:47 | +10 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-04 19:47 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 11-04 19:47 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-04 19:47 | +20 | ETH | DOWN | 0.63 | 0.88 | 2.25 |
| 11-04 19:47 | +15 | ETH | DOWN | 0.63 | 0.88 | 2.25 |
| 11-04 19:47 | +10 | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-04 19:47 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 19:47 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-04 19:47 | +20 | ZEC | DOWN | 0.64 | 0.88 | 2.15 |
| 11-04 19:47 | +15 | ZEC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-04 19:47 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-04 19:47 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 11-04 19:47 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.76 |
| 11-04 19:47 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.92 |
| 11-04 19:47 | +15 | BNB | DOWN | 0.68 | 0.89 | 1.92 |
| 11-04 19:47 | +10 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-04 19:47 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-04 19:34 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-04 19:33 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.81 |
| 11-04 19:32 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-04 19:32 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-04 19:32 | +15 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-04 19:32 | +10 | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-04 19:32 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-04 19:32 | +10 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-04 19:32 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
