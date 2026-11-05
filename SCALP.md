# Range-Scalp Bot

*Updated Thu Nov 05 00:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47791 | 41617 | 6174 (73) | 2 | $-13764.12 | -4.6% |
| **+10¢** | 35705 | 28542 | 7163 (98) | 5 | $-12584.29 | -5.6% |
| **+15¢** | 29915 | 22202 | 7713 (126) | 6 | $-11511.68 | -6.1% |
| **+20¢** | 26579 | 18502 | 8077 (166) | 7 | $-10139.61 | -6.1% |
| **+10¢ (15¢ stop)** | 58261 | 58168 | 93 (56) | 0 | $-21653.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 00:56 | +10 stop | SOL | DOWN | 0.59 | 0.85 | 2.34 |
| 11-05 00:56 | +15 | SOL | DOWN | 0.58 | 0.85 | 2.43 |
| 11-05 00:56 | +10 | SOL | DOWN | 0.58 | 0.85 | 2.43 |
| 11-05 00:54 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-05 00:53 | +10 stop | DOGE | UP | 0.61 | 0.42 | -2.25 |
| 11-05 00:53 | +20 | DOGE | UP | 0.61 | open |  |
| 11-05 00:53 | +15 | DOGE | UP | 0.61 | open |  |
| 11-05 00:53 | +10 | DOGE | UP | 0.61 | open |  |
| 11-05 00:53 | +5 | DOGE | UP | 0.61 | open |  |
| 11-05 00:52 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-05 00:52 | +5 | XRP | UP | 0.61 | open |  |
| 11-05 00:52 | +5 | NEAR | UP | 0.56 | 0.61 | 0.15 |
| 11-05 00:52 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 11-05 00:52 | +10 stop | ZEC | UP | 0.55 | 0.32 | -2.64 |
| 11-05 00:52 | +20 | ZEC | UP | 0.55 | open |  |
| 11-05 00:52 | +15 | ZEC | UP | 0.55 | open |  |
| 11-05 00:52 | +10 | ZEC | UP | 0.55 | open |  |
| 11-05 00:51 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.50 |
| 11-05 00:51 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.67 |
| 11-05 00:51 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 11-05 00:51 | +20 | NEAR | UP | 0.59 | open |  |
| 11-05 00:51 | +15 | NEAR | UP | 0.59 | open |  |
| 11-05 00:51 | +10 | NEAR | UP | 0.59 | open |  |
| 11-05 00:51 | +5 | NEAR | UP | 0.59 | 0.66 | 0.37 |
| 11-05 00:51 | +15 | ETH | UP | 0.59 | open |  |
| 11-05 00:51 | +10 stop | ETH | UP | 0.63 | 0.43 | -2.35 |
| 11-05 00:51 | +10 | ETH | UP | 0.63 | open |  |
| 11-05 00:50 | +10 stop | HYPE | UP | 0.47 | 0.31 | -1.93 |
| 11-05 00:50 | +10 stop | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-05 00:50 | +5 | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-05 00:50 | +5 | BTC | DOWN | 0.54 | 0.62 | 0.45 |
| 11-05 00:50 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-05 00:49 | +10 stop | ETH | DOWN | 0.53 | 0.65 | 0.86 |
| 11-05 00:49 | +10 | ETH | DOWN | 0.53 | 0.65 | 0.86 |
| 11-05 00:49 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.01 |
| 11-05 00:49 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.26 |
| 11-05 00:49 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.37 |
| 11-05 00:49 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-05 00:49 | +20 | SOL | UP | 0.71 | open |  |
| 11-05 00:49 | +15 | SOL | UP | 0.71 | 0.87 | 1.37 |
