# Range-Scalp Bot

*Updated Wed Nov 18 09:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63919 | 55749 | 8170 (119) | 6 | $-17470.31 | -4.3% |
| **+10¢** | 47746 | 38182 | 9564 (160) | 7 | $-16391.84 | -5.5% |
| **+15¢** | 40033 | 29722 | 10311 (205) | 9 | $-14858.12 | -5.9% |
| **+20¢** | 35654 | 24830 | 10824 (260) | 9 | $-13159.40 | -5.9% |
| **+10¢ (15¢ stop)** | 77750 | 77592 | 158 (93) | 6 | $-28549.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 09:21 | +5 | DOGE | UP | 0.62 | open |  |
| 11-18 09:21 | +10 stop | ETH | UP | 0.52 | open |  |
| 11-18 09:21 | +5 | DOGE | UP | 0.60 | 0.66 | 0.27 |
| 11-18 09:20 | +5 | ZEC | UP | 0.63 | open |  |
| 11-18 09:20 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 11-18 09:20 | +5 | DOGE | UP | 0.52 | 0.63 | 0.75 |
| 11-18 09:19 | +5 | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 11-18 09:19 | +10 stop | DOGE | UP | 0.65 | open |  |
| 11-18 09:19 | +10 stop | ETH | DOWN | 0.58 | 0.41 | -2.05 |
| 11-18 09:19 | +5 | ETH | DOWN | 0.57 | open |  |
| 11-18 09:19 | +10 stop | SOL | DOWN | 0.57 | open |  |
| 11-18 09:19 | +5 | SOL | DOWN | 0.57 | 0.63 | 0.25 |
| 11-18 09:18 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-18 09:18 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-18 09:18 | +10 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-18 09:18 | +5 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-18 09:18 | +10 stop | XRP | DOWN | 0.50 | 0.35 | -1.84 |
| 11-18 09:18 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 11-18 09:18 | +10 stop | ZEC | UP | 0.53 | open |  |
| 11-18 09:18 | +20 | ZEC | UP | 0.53 | open |  |
| 11-18 09:18 | +15 | ZEC | UP | 0.53 | open |  |
| 11-18 09:18 | +10 | ZEC | UP | 0.54 | open |  |
| 11-18 09:18 | +5 | ZEC | UP | 0.52 | 0.58 | 0.24 |
| 11-18 09:18 | +5 | DOGE | UP | 0.57 | 0.64 | 0.35 |
| 11-18 09:18 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-18 09:18 | +5 | ETH | UP | 0.51 | 0.59 | 0.45 |
| 11-18 09:17 | +10 stop | BTC | UP | 0.71 | 0.51 | -2.33 |
| 11-18 09:17 | +10 | BTC | UP | 0.71 | open |  |
| 11-18 09:17 | +5 | BTC | UP | 0.71 | open |  |
| 11-18 09:17 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 11-18 09:17 | +20 | HYPE | UP | 0.68 | open |  |
| 11-18 09:17 | +15 | HYPE | UP | 0.68 | open |  |
| 11-18 09:17 | +10 | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 11-18 09:17 | +5 | HYPE | UP | 0.68 | 0.77 | 0.61 |
| 11-18 09:16 | +10 stop | XRP | UP | 0.67 | 0.44 | -2.64 |
| 11-18 09:16 | +20 | XRP | UP | 0.67 | open |  |
| 11-18 09:16 | +15 | XRP | UP | 0.66 | open |  |
| 11-18 09:16 | +10 | XRP | UP | 0.66 | open |  |
| 11-18 09:16 | +5 | XRP | UP | 0.66 | open |  |
| 11-18 09:16 | +10 stop | SOL | UP | 0.68 | 0.50 | -2.14 |
