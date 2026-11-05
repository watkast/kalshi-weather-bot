# Range-Scalp Bot

*Updated Thu Nov 05 05:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48069 | 41861 | 6208 (73) | 1 | $-13841.25 | -4.6% |
| **+10¢** | 35909 | 28697 | 7212 (99) | 1 | $-12708.01 | -5.6% |
| **+15¢** | 30089 | 22326 | 7763 (127) | 1 | $-11608.26 | -6.1% |
| **+20¢** | 26730 | 18598 | 8132 (166) | 1 | $-10271.29 | -6.1% |
| **+10¢ (15¢ stop)** | 58594 | 58501 | 93 (56) | 0 | $-21771.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 05:06 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-05 05:06 | +10 | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-05 05:06 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 05:06 | +5 | HYPE | DOWN | 0.68 | 0.77 | 0.61 |
| 11-05 05:05 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 11-05 05:05 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-05 05:05 | +10 stop | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 11-05 05:05 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-05 05:05 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-05 05:05 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-05 05:05 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-05 05:04 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 05:04 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 11-05 05:04 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-05 05:04 | +10 stop | ETH | UP | 0.57 | 0.42 | -1.86 |
| 11-05 05:04 | +5 | HYPE | UP | 0.59 | 0.67 | 0.47 |
| 11-05 05:04 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-05 05:04 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-05 05:04 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-05 05:04 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-05 05:04 | +5 | BNB | DOWN | 0.69 | 0.75 | 0.31 |
| 11-05 05:03 | +10 stop | HYPE | UP | 0.69 | 0.52 | -2.03 |
| 11-05 05:03 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 11-05 05:03 | +20 | SOL | UP | 0.64 | open |  |
| 11-05 05:03 | +15 | SOL | UP | 0.64 | open |  |
| 11-05 05:03 | +10 | SOL | UP | 0.64 | open |  |
| 11-05 05:03 | +5 | SOL | UP | 0.64 | open |  |
| 11-05 05:03 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-05 05:03 | +20 | ZEC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-05 05:03 | +15 | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-05 05:03 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 05:03 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-05 05:03 | +10 stop | ETH | DOWN | 0.52 | 0.36 | -1.95 |
| 11-05 05:03 | +20 | ETH | DOWN | 0.52 | 0.76 | 2.09 |
| 11-05 05:03 | +15 | ETH | DOWN | 0.52 | 0.69 | 1.37 |
| 11-05 05:03 | +10 | ETH | DOWN | 0.52 | 0.64 | 0.85 |
| 11-05 05:03 | +5 | ETH | DOWN | 0.52 | 0.64 | 0.85 |
| 11-05 05:03 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-05 05:03 | +20 | DOGE | DOWN | 0.55 | 0.75 | 1.68 |
| 11-05 05:03 | +15 | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
