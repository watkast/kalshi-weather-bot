# Range-Scalp Bot

*Updated Thu Oct 29 16:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39425 | 34417 | 5008 (50) | 2 | $-10963.84 | -4.4% |
| **+10¢** | 29389 | 23603 | 5786 (73) | 5 | $-9701.37 | -5.2% |
| **+15¢** | 24572 | 18354 | 6218 (100) | 5 | $-8666.54 | -5.6% |
| **+20¢** | 21801 | 15287 | 6514 (129) | 6 | $-7556.74 | -5.5% |
| **+10¢ (15¢ stop)** | 48163 | 48093 | 70 (37) | 4 | $-18262.64 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 16:17 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 10-29 16:17 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-29 16:17 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-29 16:17 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-29 16:17 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-29 16:16 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-29 16:16 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-29 16:16 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-29 16:16 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-29 16:16 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-29 16:16 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-29 16:16 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 10-29 16:16 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-29 16:16 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-29 16:16 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-29 16:16 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-29 16:16 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-29 16:16 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-29 16:16 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-29 16:16 | +10 | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-29 16:16 | +5 | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-29 16:15 | +10 stop | NEAR | UP | 0.55 | 0.38 | -2.05 |
| 10-29 16:15 | +20 | NEAR | UP | 0.55 | open |  |
| 10-29 16:15 | +15 | NEAR | UP | 0.55 | open |  |
| 10-29 16:15 | +10 | NEAR | UP | 0.53 | open |  |
| 10-29 16:15 | +5 | NEAR | UP | 0.53 | open |  |
| 10-29 16:13 | +10 stop | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 10-29 16:13 | +15 | SOL | DOWN | 0.71 | 0.91 | 1.76 |
| 10-29 16:13 | +10 | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 10-29 16:13 | +5 | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 10-29 16:12 | +10 stop | ETH | UP | 0.52 | 0.15 | -3.97 |
| 10-29 16:12 | +10 stop | SOL | UP | 0.49 | 0.68 | 1.56 |
| 10-29 16:12 | +5 | SOL | UP | 0.47 | 0.68 | 1.76 |
| 10-29 16:12 | +10 stop | BTC | UP | 0.34 | 0.65 | 2.78 |
| 10-29 16:12 | +20 | BTC | UP | 0.34 | 0.65 | 2.78 |
| 10-29 16:12 | +15 | BTC | UP | 0.35 | 0.65 | 2.68 |
| 10-29 16:12 | +10 | BTC | UP | 0.35 | 0.65 | 2.68 |
| 10-29 16:12 | +5 | BTC | UP | 0.35 | 0.65 | 2.68 |
| 10-29 16:07 | +5 | BTC | UP | 0.68 | 0.80 | 0.92 |
| 10-29 16:07 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
