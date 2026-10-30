# Range-Scalp Bot

*Updated Fri Oct 30 22:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41327 | 36069 | 5258 (54) | 1 | $-11541.52 | -4.4% |
| **+10¢** | 30806 | 24721 | 6085 (78) | 2 | $-10283.30 | -5.3% |
| **+15¢** | 25750 | 19194 | 6556 (106) | 2 | $-9332.76 | -5.8% |
| **+20¢** | 22854 | 15988 | 6866 (137) | 2 | $-8208.00 | -5.7% |
| **+10¢ (15¢ stop)** | 50382 | 50307 | 75 (41) | 2 | $-19031.43 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 22:06 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 10-30 22:06 | +10 stop | NEAR | UP | 0.55 | open |  |
| 10-30 22:06 | +20 | NEAR | UP | 0.55 | open |  |
| 10-30 22:06 | +15 | NEAR | UP | 0.55 | open |  |
| 10-30 22:06 | +10 | NEAR | UP | 0.55 | open |  |
| 10-30 22:06 | +5 | NEAR | UP | 0.55 | 0.60 | 0.15 |
| 10-30 22:03 | +10 stop | HYPE | UP | 0.61 | 0.44 | -2.08 |
| 10-30 22:03 | +10 | HYPE | UP | 0.61 | open |  |
| 10-30 22:03 | +5 | HYPE | UP | 0.61 | open |  |
| 10-30 22:02 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.93 |
| 10-30 22:02 | +20 | ZEC | UP | 0.66 | 0.87 | 1.86 |
| 10-30 22:02 | +15 | ZEC | UP | 0.66 | 0.84 | 1.54 |
| 10-30 22:02 | +10 | ZEC | UP | 0.65 | 0.78 | 1.03 |
| 10-30 22:02 | +5 | ZEC | UP | 0.64 | 0.78 | 1.10 |
| 10-30 22:02 | +10 stop | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 10-30 22:02 | +20 | NEAR | UP | 0.64 | 0.85 | 1.84 |
| 10-30 22:02 | +15 | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 10-30 22:02 | +10 | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 10-30 22:02 | +5 | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 10-30 22:01 | +10 stop | HYPE | UP | 0.56 | 0.68 | 0.86 |
| 10-30 22:01 | +20 | HYPE | UP | 0.56 | open |  |
| 10-30 22:01 | +15 | HYPE | UP | 0.56 | open |  |
| 10-30 22:01 | +10 | HYPE | UP | 0.56 | 0.68 | 0.86 |
| 10-30 22:01 | +5 | HYPE | UP | 0.56 | 0.61 | 0.15 |
| 10-30 22:01 | +10 stop | BNB | UP | 0.70 | 0.87 | 1.47 |
| 10-30 22:01 | +20 | BNB | UP | 0.70 | 0.92 | 1.99 |
| 10-30 22:01 | +15 | BNB | UP | 0.70 | 0.87 | 1.47 |
| 10-30 22:01 | +10 | BNB | UP | 0.70 | 0.87 | 1.47 |
| 10-30 22:01 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 10-30 22:01 | +10 stop | SOL | UP | 0.63 | 0.78 | 1.20 |
| 10-30 22:01 | +20 | SOL | UP | 0.63 | 0.86 | 2.04 |
| 10-30 22:01 | +15 | SOL | UP | 0.63 | 0.78 | 1.20 |
| 10-30 22:01 | +10 | SOL | UP | 0.63 | 0.78 | 1.20 |
| 10-30 22:01 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 10-30 21:50 | +10 stop | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-30 21:50 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 10-30 21:49 | +10 stop | SOL | DOWN | 0.59 | 0.83 | 2.13 |
| 10-30 21:48 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 21:48 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 21:48 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
