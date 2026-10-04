# Range-Scalp Bot

*Updated Sun Oct 04 20:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2775 | 2389 | 386 (3) | 4 | $-937.35 | -5.3% |
| **+10¢** | 2167 | 1733 | 434 (4) | 4 | $-769.35 | -5.6% |
| **+15¢** | 1818 | 1360 | 458 (5) | 4 | $-647.96 | -5.7% |
| **+20¢** | 1617 | 1137 | 480 (9) | 5 | $-561.05 | -5.5% |
| **+10¢ (15¢ stop)** | 3443 | 3442 | 1 (1) | 4 | $-1312.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 20:32 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-04 20:32 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-04 20:32 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-04 20:31 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-04 20:31 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-04 20:31 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-04 20:31 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-04 20:31 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-04 20:31 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 10-04 20:31 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-04 20:30 | +10 stop | SOL | UP | 0.59 | 0.37 | -2.58 |
| 10-04 20:30 | +20 | SOL | UP | 0.58 | open |  |
| 10-04 20:30 | +15 | SOL | UP | 0.58 | open |  |
| 10-04 20:30 | +10 | SOL | UP | 0.58 | open |  |
| 10-04 20:30 | +5 | SOL | UP | 0.58 | open |  |
| 10-04 20:30 | +10 stop | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-04 20:30 | +20 | DOGE | DOWN | 0.60 | open |  |
| 10-04 20:30 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-04 20:30 | +10 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-04 20:30 | +5 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-04 20:30 | +10 stop | NEAR | UP | 0.48 | open |  |
| 10-04 20:30 | +20 | NEAR | UP | 0.48 | open |  |
| 10-04 20:30 | +15 | NEAR | UP | 0.48 | open |  |
| 10-04 20:30 | +10 | NEAR | UP | 0.48 | open |  |
| 10-04 20:30 | +5 | NEAR | UP | 0.48 | 0.55 | 0.34 |
| 10-04 20:30 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 20:30 | +20 | HYPE | DOWN | 0.58 | open |  |
| 10-04 20:30 | +15 | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-04 20:30 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 20:30 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 20:26 | +10 stop | NEAR | UP | 0.67 | 0.81 | 1.18 |
| 10-04 20:26 | +20 | NEAR | UP | 0.67 | 0.93 | 2.46 |
| 10-04 20:26 | +15 | NEAR | UP | 0.67 | 0.93 | 2.46 |
| 10-04 20:26 | +10 | NEAR | UP | 0.67 | 0.81 | 1.18 |
| 10-04 20:26 | +5 | NEAR | UP | 0.67 | 0.75 | 0.55 |
| 10-04 20:24 | +10 stop | HYPE | DOWN | 0.67 | 0.15 | -5.40 |
| 10-04 20:23 | +10 stop | XRP | DOWN | 0.55 | 0.75 | 1.66 |
| 10-04 20:23 | +10 | XRP | DOWN | 0.55 | 0.75 | 1.68 |
| 10-04 20:23 | +5 | XRP | DOWN | 0.55 | 0.61 | 0.22 |
| 10-04 20:22 | +10 stop | SOL | UP | 0.71 | 0.45 | -2.93 |
