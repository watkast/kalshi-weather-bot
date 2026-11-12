# Range-Scalp Bot

*Updated Thu Nov 12 05:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56663 | 49394 | 7269 (98) | 2 | $-15627.83 | -4.4% |
| **+10¢** | 42345 | 33865 | 8480 (128) | 2 | $-14582.02 | -5.5% |
| **+15¢** | 35503 | 26373 | 9130 (162) | 2 | $-13225.83 | -5.9% |
| **+20¢** | 31627 | 22045 | 9582 (212) | 3 | $-11629.84 | -5.9% |
| **+10¢ (15¢ stop)** | 69084 | 68961 | 123 (73) | 2 | $-25511.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 05:06 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 11-12 05:06 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-12 05:06 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-12 05:06 | +5 | DOGE | DOWN | 0.64 | open |  |
| 11-12 05:03 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-12 05:02 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 05:02 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-12 05:02 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-12 05:02 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 05:02 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-12 05:02 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 05:02 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-12 05:02 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-12 05:02 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 05:02 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-12 05:02 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 11-12 05:02 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-12 05:02 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-12 05:02 | +10 | ZEC | DOWN | 0.67 | open |  |
| 11-12 05:02 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-12 04:58 | +10 stop | BTC | UP | 0.48 | 0.73 | 2.18 |
| 11-12 04:58 | +20 | BTC | UP | 0.48 | 0.73 | 2.18 |
| 11-12 04:58 | +15 | BTC | UP | 0.48 | 0.73 | 2.18 |
| 11-12 04:58 | +10 | BTC | UP | 0.48 | 0.73 | 2.18 |
| 11-12 04:58 | +5 | BTC | UP | 0.51 | 0.73 | 1.88 |
| 11-12 04:58 | +10 stop | DOGE | DOWN | 0.60 | 0.83 | 2.03 |
| 11-12 04:58 | +5 | DOGE | DOWN | 0.61 | 0.83 | 1.93 |
| 11-12 04:58 | +5 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 04:57 | +10 stop | ETH | UP | 0.56 | 0.36 | -2.35 |
| 11-12 04:57 | +20 | ETH | UP | 0.56 | no | -5.78 |
| 11-12 04:57 | +15 | ETH | UP | 0.56 | no | -5.78 |
| 11-12 04:57 | +10 | ETH | UP | 0.56 | no | -5.78 |
| 11-12 04:57 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 11-12 04:56 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-12 04:56 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.41 |
| 11-12 04:56 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.41 |
| 11-12 04:56 | +10 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-12 04:56 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.50 |
| 11-12 04:56 | +10 stop | DOGE | UP | 0.56 | 0.25 | -3.42 |
| 11-12 04:56 | +15 | DOGE | UP | 0.56 | no | -5.78 |
