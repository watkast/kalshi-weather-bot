# Range-Scalp Bot

*Updated Thu Nov 12 04:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56639 | 49372 | 7267 (98) | 0 | $-15630.17 | -4.4% |
| **+10¢** | 42326 | 33850 | 8476 (128) | 0 | $-14574.09 | -5.5% |
| **+15¢** | 35486 | 26361 | 9125 (162) | 0 | $-13211.02 | -5.9% |
| **+20¢** | 31616 | 22040 | 9576 (212) | 0 | $-11599.27 | -5.9% |
| **+10¢ (15¢ stop)** | 69047 | 68924 | 123 (73) | 0 | $-25494.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 04:30 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 04:30 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.98 |
| 11-12 04:30 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-12 04:30 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 04:30 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-12 04:30 | +10 stop | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-12 04:30 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-12 04:30 | +15 | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-12 04:30 | +10 | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-12 04:30 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-12 04:27 | +10 stop | ZEC | UP | 0.67 | 0.46 | -2.44 |
| 11-12 04:26 | +10 stop | ZEC | DOWN | 0.63 | 0.42 | -2.45 |
| 11-12 04:26 | +15 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 11-12 04:26 | +10 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 11-12 04:26 | +5 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 11-12 04:26 | +10 stop | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-12 04:26 | +10 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-12 04:26 | +5 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 11-12 04:23 | +10 stop | NEAR | DOWN | 0.55 | 0.70 | 1.17 |
| 11-12 04:23 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 04:23 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 11-12 04:23 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 04:23 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-12 04:23 | +10 stop | HYPE | DOWN | 0.54 | 0.75 | 1.78 |
| 11-12 04:23 | +5 | HYPE | DOWN | 0.54 | 0.61 | 0.35 |
| 11-12 04:22 | +10 stop | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 04:22 | +20 | BNB | DOWN | 0.68 | 0.92 | 2.23 |
| 11-12 04:22 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 04:22 | +10 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 04:22 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 04:21 | +10 stop | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 04:21 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-12 04:21 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-12 04:20 | +5 | NEAR | UP | 0.62 | no | -6.37 |
| 11-12 04:20 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 11-12 04:20 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 04:20 | +5 | DOGE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-12 04:19 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 04:19 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 04:19 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
