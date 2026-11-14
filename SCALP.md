# Range-Scalp Bot

*Updated Sat Nov 14 00:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58766 | 51274 | 7492 (106) | 3 | $-15873.58 | -4.3% |
| **+10¢** | 43900 | 35139 | 8761 (139) | 5 | $-14848.02 | -5.4% |
| **+15¢** | 36790 | 27353 | 9437 (174) | 7 | $-13427.75 | -5.8% |
| **+20¢** | 32775 | 22868 | 9907 (225) | 7 | $-11816.50 | -5.7% |
| **+10¢ (15¢ stop)** | 71545 | 71407 | 138 (82) | 3 | $-26349.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 00:36 | +10 stop | XRP | DOWN | 0.71 | open |  |
| 11-14 00:36 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-14 00:36 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-14 00:36 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-14 00:36 | +5 | XRP | DOWN | 0.67 | open |  |
| 11-14 00:36 | +10 stop | HYPE | DOWN | 0.57 | open |  |
| 11-14 00:36 | +10 | HYPE | DOWN | 0.57 | open |  |
| 11-14 00:36 | +5 | HYPE | DOWN | 0.57 | open |  |
| 11-14 00:35 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 11-14 00:35 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
| 11-14 00:32 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-14 00:32 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 11-14 00:32 | +10 stop | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-14 00:32 | +5 | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-14 00:32 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.50 |
| 11-14 00:31 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-14 00:31 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-14 00:31 | +15 | HYPE | DOWN | 0.71 | open |  |
| 11-14 00:31 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-14 00:31 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-14 00:31 | +5 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 00:31 | +10 stop | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-14 00:31 | +20 | SOL | UP | 0.53 | open |  |
| 11-14 00:31 | +15 | SOL | UP | 0.53 | open |  |
| 11-14 00:31 | +10 | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-14 00:31 | +5 | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-14 00:31 | +10 stop | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 11-14 00:31 | +20 | NEAR | UP | 0.53 | open |  |
| 11-14 00:31 | +15 | NEAR | UP | 0.53 | open |  |
| 11-14 00:31 | +10 | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 11-14 00:31 | +5 | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 11-14 00:31 | +10 stop | BNB | UP | 0.51 | 0.30 | -2.43 |
| 11-14 00:31 | +20 | BNB | UP | 0.51 | open |  |
| 11-14 00:31 | +15 | BNB | UP | 0.51 | open |  |
| 11-14 00:31 | +10 | BNB | UP | 0.51 | open |  |
| 11-14 00:31 | +5 | BNB | UP | 0.51 | 0.59 | 0.45 |
| 11-14 00:31 | +10 stop | DOGE | UP | 0.55 | 0.35 | -2.34 |
| 11-14 00:31 | +20 | DOGE | UP | 0.54 | open |  |
| 11-14 00:31 | +15 | DOGE | UP | 0.54 | open |  |
| 11-14 00:31 | +10 | DOGE | UP | 0.54 | open |  |
