# Range-Scalp Bot

*Updated Thu Oct 22 00:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27971 | 24371 | 3600 (39) | 7 | $-8047.55 | -4.6% |
| **+10¢** | 21012 | 16855 | 4157 (55) | 7 | $-7082.84 | -5.4% |
| **+15¢** | 17601 | 13127 | 4474 (78) | 7 | $-6313.35 | -5.7% |
| **+20¢** | 15581 | 10893 | 4688 (98) | 8 | $-5638.47 | -5.8% |
| **+10¢ (15¢ stop)** | 34343 | 34284 | 59 (32) | 2 | $-12841.77 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 00:35 | +10 stop | BTC | UP | 0.63 | open |  |
| 10-22 00:34 | +10 stop | XRP | DOWN | 0.55 | open |  |
| 10-22 00:34 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-22 00:34 | +10 stop | DOGE | DOWN | 0.58 | 0.38 | -2.35 |
| 10-22 00:34 | +10 stop | BNB | DOWN | 0.69 | 0.52 | -2.03 |
| 10-22 00:34 | +10 stop | BNB | UP | 0.44 | 0.57 | 0.94 |
| 10-22 00:33 | +10 stop | DOGE | UP | 0.63 | 0.43 | -2.35 |
| 10-22 00:33 | +10 stop | ETH | UP | 0.65 | 0.40 | -2.83 |
| 10-22 00:33 | +10 stop | SOL | UP | 0.62 | 0.42 | -2.35 |
| 10-22 00:33 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 10-22 00:33 | +10 stop | HYPE | UP | 0.68 | 0.47 | -2.44 |
| 10-22 00:33 | +5 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 10-22 00:33 | +5 | BTC | UP | 0.69 | open |  |
| 10-22 00:32 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 10-22 00:32 | +10 stop | BTC | DOWN | 0.47 | 0.32 | -1.84 |
| 10-22 00:32 | +20 | BTC | DOWN | 0.47 | open |  |
| 10-22 00:32 | +15 | BTC | DOWN | 0.47 | open |  |
| 10-22 00:32 | +10 | BTC | DOWN | 0.47 | open |  |
| 10-22 00:32 | +5 | BTC | DOWN | 0.47 | 0.55 | 0.44 |
| 10-22 00:32 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-22 00:32 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-22 00:31 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-22 00:31 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 10-22 00:31 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-22 00:31 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-22 00:31 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-22 00:31 | +5 | ETH | DOWN | 0.57 | open |  |
| 10-22 00:31 | +10 stop | DOGE | DOWN | 0.68 | 0.50 | -2.14 |
| 10-22 00:31 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-22 00:31 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-22 00:31 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-22 00:31 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-22 00:31 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 10-22 00:31 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-22 00:31 | +15 | NEAR | DOWN | 0.64 | 0.82 | 1.52 |
| 10-22 00:31 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 10-22 00:31 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 10-22 00:31 | +10 stop | BNB | DOWN | 0.62 | 0.44 | -2.15 |
| 10-22 00:31 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-22 00:31 | +15 | BNB | DOWN | 0.62 | open |  |
