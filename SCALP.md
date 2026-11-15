# Range-Scalp Bot

*Updated Sun Nov 15 21:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61213 | 53412 | 7801 (114) | 1 | $-16497.54 | -4.3% |
| **+10¢** | 45719 | 36580 | 9139 (153) | 5 | $-15482.08 | -5.4% |
| **+15¢** | 38297 | 28442 | 9855 (191) | 5 | $-14116.36 | -5.9% |
| **+20¢** | 34135 | 23797 | 10338 (243) | 5 | $-12386.64 | -5.8% |
| **+10¢ (15¢ stop)** | 74492 | 74340 | 152 (90) | 4 | $-27410.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 21:01 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 11-15 21:01 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-15 21:01 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-15 21:01 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-15 21:01 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 11-15 21:01 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 11-15 21:01 | +20 | XRP | DOWN | 0.56 | open |  |
| 11-15 21:01 | +15 | XRP | DOWN | 0.56 | open |  |
| 11-15 21:01 | +10 | XRP | DOWN | 0.56 | open |  |
| 11-15 21:01 | +5 | XRP | DOWN | 0.56 | 0.61 | 0.15 |
| 11-15 21:01 | +10 stop | DOGE | DOWN | 0.51 | open |  |
| 11-15 21:01 | +20 | DOGE | DOWN | 0.51 | open |  |
| 11-15 21:01 | +15 | DOGE | DOWN | 0.51 | open |  |
| 11-15 21:01 | +10 | DOGE | DOWN | 0.51 | open |  |
| 11-15 21:01 | +5 | DOGE | DOWN | 0.51 | 0.58 | 0.34 |
| 11-15 21:01 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 11-15 21:01 | +20 | ETH | DOWN | 0.57 | open |  |
| 11-15 21:01 | +15 | ETH | DOWN | 0.58 | open |  |
| 11-15 21:01 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-15 21:01 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 11-15 21:00 | +10 stop | BNB | DOWN | 0.71 | 0.55 | -1.93 |
| 11-15 21:00 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-15 21:00 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-15 21:00 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-15 21:00 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-15 20:57 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 20:57 | +10 stop | SOL | DOWN | 0.56 | 0.92 | 3.37 |
| 11-15 20:56 | +10 stop | XRP | UP | 0.19 | 0.54 | 3.19 |
| 11-15 20:56 | +10 stop | DOGE | UP | 0.35 | 0.64 | 2.59 |
| 11-15 20:56 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 11-15 20:56 | +20 | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 20:56 | +15 | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 20:56 | +10 | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 20:56 | +10 stop | SOL | DOWN | 0.63 | 0.38 | -2.84 |
| 11-15 20:56 | +5 | SOL | DOWN | 0.63 | 0.92 | 2.68 |
| 11-15 20:55 | +10 stop | DOGE | DOWN | 0.69 | 0.45 | -2.73 |
| 11-15 20:54 | +5 | XRP | UP | 0.54 | no | -5.58 |
| 11-15 20:53 | +10 stop | SOL | DOWN | 0.57 | 0.73 | 1.28 |
| 11-15 20:53 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-15 20:53 | +10 stop | XRP | DOWN | 0.52 | 0.65 | 0.97 |
