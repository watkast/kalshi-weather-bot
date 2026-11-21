# Range-Scalp Bot

*Updated Sat Nov 21 16:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67568 | 58970 | 8598 (134) | 6 | $-18135.25 | -4.3% |
| **+10¢** | 50461 | 40414 | 10047 (175) | 5 | $-16840.70 | -5.3% |
| **+15¢** | 42307 | 31476 | 10831 (225) | 6 | $-15097.62 | -5.7% |
| **+20¢** | 37655 | 26274 | 11381 (283) | 8 | $-13414.50 | -5.7% |
| **+10¢ (15¢ stop)** | 82251 | 82080 | 171 (105) | 4 | $-30200.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 16:07 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-21 16:07 | +10 stop | NEAR | UP | 0.56 | open |  |
| 11-21 16:07 | +10 | NEAR | UP | 0.58 | open |  |
| 11-21 16:07 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 11-21 16:07 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-21 16:07 | +10 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 11-21 16:07 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 11-21 16:07 | +10 stop | ZEC | UP | 0.67 | 0.49 | -2.14 |
| 11-21 16:06 | +10 stop | HYPE | DOWN | 0.57 | open |  |
| 11-21 16:06 | +10 stop | BTC | DOWN | 0.54 | open |  |
| 11-21 16:06 | +10 stop | BTC | DOWN | 0.51 | 0.68 | 1.36 |
| 11-21 16:05 | +10 stop | XRP | UP | 0.56 | 0.74 | 1.48 |
| 11-21 16:05 | +10 stop | NEAR | DOWN | 0.51 | 0.65 | 1.05 |
| 11-21 16:05 | +10 | NEAR | DOWN | 0.51 | 0.65 | 1.06 |
| 11-21 16:04 | +10 stop | HYPE | DOWN | 0.69 | 0.52 | -2.03 |
| 11-21 16:04 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-21 16:04 | +10 stop | ZEC | DOWN | 0.69 | 0.34 | -3.81 |
| 11-21 16:04 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-21 16:03 | +10 stop | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-21 16:03 | +20 | NEAR | DOWN | 0.55 | open |  |
| 11-21 16:03 | +15 | NEAR | DOWN | 0.55 | open |  |
| 11-21 16:03 | +10 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-21 16:03 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 11-21 16:03 | +10 stop | ZEC | UP | 0.59 | 0.41 | -2.14 |
| 11-21 16:03 | +10 stop | BTC | UP | 0.52 | 0.35 | -2.04 |
| 11-21 16:02 | +5 | ZEC | UP | 0.68 | open |  |
| 11-21 16:02 | +10 stop | HYPE | UP | 0.52 | 0.35 | -2.04 |
| 11-21 16:01 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.71 |
| 11-21 16:01 | +20 | SOL | DOWN | 0.65 | 0.85 | 1.76 |
| 11-21 16:01 | +15 | SOL | DOWN | 0.65 | 0.84 | 1.65 |
| 11-21 16:01 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.71 |
| 11-21 16:01 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.30 |
| 11-21 16:01 | +10 stop | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-21 16:01 | +20 | BNB | DOWN | 0.59 | open |  |
| 11-21 16:01 | +15 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 11-21 16:01 | +10 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 11-21 16:01 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.36 |
| 11-21 16:01 | +10 stop | XRP | DOWN | 0.55 | 0.39 | -1.95 |
| 11-21 16:01 | +10 stop | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 11-21 16:01 | +20 | ZEC | UP | 0.58 | open |  |
