# Range-Scalp Bot

*Updated Sun Oct 04 04:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1765 | 1520 | 245 (3) | 4 | $-602.09 | -5.4% |
| **+10¢** | 1371 | 1100 | 271 (4) | 5 | $-434.04 | -5.0% |
| **+15¢** | 1154 | 869 | 285 (5) | 5 | $-357.87 | -4.9% |
| **+20¢** | 1015 | 711 | 304 (7) | 6 | $-365.36 | -5.7% |
| **+10¢ (15¢ stop)** | 2237 | 2236 | 1 (1) | 1 | $-950.84 | -6.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 04:40 | +5 | HYPE | UP | 0.57 | open |  |
| 10-04 04:39 | +10 stop | HYPE | UP | 0.69 | 0.53 | -1.93 |
| 10-04 04:38 | +5 | BNB | UP | 0.64 | 0.70 | 0.28 |
| 10-04 04:37 | +10 stop | BNB | UP | 0.58 | 0.70 | 0.88 |
| 10-04 04:36 | +10 stop | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 10-04 04:36 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-04 04:36 | +10 stop | HYPE | DOWN | 0.69 | 0.51 | -2.13 |
| 10-04 04:35 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 10-04 04:35 | +10 stop | DOGE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-04 04:35 | +10 stop | SOL | UP | 0.62 | 0.40 | -2.54 |
| 10-04 04:35 | +10 | SOL | UP | 0.62 | open |  |
| 10-04 04:35 | +5 | SOL | UP | 0.62 | open |  |
| 10-04 04:35 | +10 stop | ZEC | DOWN | 0.57 | 0.38 | -2.28 |
| 10-04 04:35 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 10-04 04:35 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-04 04:35 | +15 | BTC | DOWN | 0.58 | open |  |
| 10-04 04:35 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-04 04:35 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-04 04:34 | +10 stop | DOGE | UP | 0.61 | 0.41 | -2.34 |
| 10-04 04:34 | +10 | DOGE | UP | 0.61 | open |  |
| 10-04 04:34 | +5 | DOGE | UP | 0.61 | open |  |
| 10-04 04:33 | +10 stop | BNB | DOWN | 0.59 | 0.43 | -2.00 |
| 10-04 04:33 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 04:33 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-04 04:33 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-04 04:33 | +10 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-04 04:33 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-04 04:32 | +10 stop | HYPE | UP | 0.58 | 0.43 | -1.90 |
| 10-04 04:32 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-04 04:32 | +20 | SOL | UP | 0.63 | open |  |
| 10-04 04:32 | +15 | SOL | UP | 0.63 | open |  |
| 10-04 04:32 | +10 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-04 04:32 | +5 | SOL | UP | 0.63 | 0.70 | 0.38 |
| 10-04 04:32 | +10 stop | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 10-04 04:32 | +20 | NEAR | UP | 0.70 | 0.94 | 2.16 |
| 10-04 04:32 | +15 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 10-04 04:32 | +10 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 10-04 04:32 | +5 | NEAR | UP | 0.70 | 0.78 | 0.52 |
| 10-04 04:32 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.16 |
| 10-04 04:32 | +20 | ZEC | UP | 0.63 | 0.90 | 2.48 |
