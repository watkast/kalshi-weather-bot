# Range-Scalp Bot

*Updated Thu Oct 15 22:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18258 | 15849 | 2409 (28) | 5 | $-5607.90 | -4.9% |
| **+10¢** | 13784 | 10997 | 2787 (40) | 7 | $-5063.00 | -5.8% |
| **+15¢** | 11562 | 8564 | 2998 (59) | 7 | $-4579.32 | -6.3% |
| **+20¢** | 10271 | 7137 | 3134 (78) | 6 | $-3973.91 | -6.2% |
| **+10¢ (15¢ stop)** | 22472 | 22422 | 50 (29) | 2 | $-8705.43 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 22:37 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-15 22:36 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 10-15 22:36 | +10 | BTC | DOWN | 0.50 | open |  |
| 10-15 22:36 | +5 | BTC | DOWN | 0.50 | 0.58 | 0.44 |
| 10-15 22:36 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-15 22:36 | +15 | DOGE | UP | 0.68 | open |  |
| 10-15 22:36 | +10 | DOGE | UP | 0.68 | open |  |
| 10-15 22:36 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 10-15 22:36 | +10 stop | HYPE | DOWN | 0.52 | 0.64 | 0.81 |
| 10-15 22:35 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-15 22:35 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 10-15 22:35 | +10 stop | SOL | UP | 0.52 | 0.70 | 1.47 |
| 10-15 22:35 | +10 stop | ETH | UP | 0.53 | 0.77 | 2.09 |
| 10-15 22:34 | +10 stop | HYPE | UP | 0.61 | 0.39 | -2.54 |
| 10-15 22:34 | +10 stop | XRP | DOWN | 0.60 | 0.45 | -1.85 |
| 10-15 22:34 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-15 22:34 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-15 22:34 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-15 22:34 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 10-15 22:34 | +5 | HYPE | UP | 0.61 | open |  |
| 10-15 22:33 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-15 22:33 | +10 stop | DOGE | DOWN | 0.61 | 0.29 | -3.52 |
| 10-15 22:32 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-15 22:32 | +10 stop | SOL | DOWN | 0.61 | 0.41 | -2.34 |
| 10-15 22:32 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-15 22:32 | +15 | SOL | DOWN | 0.62 | open |  |
| 10-15 22:32 | +10 | SOL | DOWN | 0.62 | open |  |
| 10-15 22:32 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-15 22:32 | +10 stop | HYPE | DOWN | 0.65 | 0.38 | -3.03 |
| 10-15 22:32 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-15 22:32 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-15 22:32 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-15 22:32 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-15 22:32 | +10 stop | NEAR | UP | 0.54 | 0.67 | 0.96 |
| 10-15 22:32 | +20 | NEAR | UP | 0.54 | 0.76 | 1.89 |
| 10-15 22:32 | +15 | NEAR | UP | 0.54 | 0.71 | 1.37 |
| 10-15 22:32 | +10 | NEAR | UP | 0.54 | 0.67 | 0.96 |
| 10-15 22:32 | +5 | NEAR | UP | 0.54 | 0.67 | 0.96 |
| 10-15 22:32 | +10 stop | ETH | DOWN | 0.64 | 0.40 | -2.74 |
| 10-15 22:32 | +20 | ETH | DOWN | 0.64 | open |  |
