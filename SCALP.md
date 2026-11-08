# Range-Scalp Bot

*Updated Sun Nov 08 01:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51798 | 45168 | 6630 (80) | 1 | $-14343.11 | -4.4% |
| **+10¢** | 38666 | 30936 | 7730 (106) | 2 | $-13331.81 | -5.5% |
| **+15¢** | 32376 | 24045 | 8331 (135) | 2 | $-12219.30 | -6.0% |
| **+20¢** | 28803 | 20069 | 8734 (180) | 2 | $-10751.07 | -6.0% |
| **+10¢ (15¢ stop)** | 63091 | 62988 | 103 (61) | 0 | $-23358.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 01:41 | +10 stop | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 01:41 | +20 | XRP | DOWN | 0.63 | 0.90 | 2.48 |
| 11-08 01:41 | +15 | XRP | DOWN | 0.63 | 0.90 | 2.48 |
| 11-08 01:41 | +10 | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 01:41 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 11-08 01:39 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 11-08 01:39 | +10 | XRP | DOWN | 0.69 | 0.82 | 1.05 |
| 11-08 01:39 | +5 | XRP | DOWN | 0.69 | 0.82 | 1.05 |
| 11-08 01:37 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
| 11-08 01:37 | +10 | BTC | UP | 0.64 | 0.75 | 0.79 |
| 11-08 01:37 | +5 | BTC | UP | 0.64 | 0.71 | 0.38 |
| 11-08 01:37 | +10 stop | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 11-08 01:37 | +10 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 11-08 01:37 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 11-08 01:37 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-08 01:37 | +10 stop | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-08 01:37 | +10 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-08 01:37 | +5 | DOGE | DOWN | 0.61 | 0.70 | 0.58 |
| 11-08 01:37 | +10 stop | XRP | DOWN | 0.52 | 0.67 | 1.16 |
| 11-08 01:36 | +10 stop | SOL | UP | 0.64 | 0.24 | -4.30 |
| 11-08 01:36 | +20 | SOL | UP | 0.64 | open |  |
| 11-08 01:36 | +15 | SOL | UP | 0.64 | open |  |
| 11-08 01:36 | +10 | SOL | UP | 0.64 | open |  |
| 11-08 01:36 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 11-08 01:36 | +10 stop | ZEC | UP | 0.64 | 0.36 | -3.14 |
| 11-08 01:34 | +10 stop | XRP | UP | 0.69 | 0.81 | 0.94 |
| 11-08 01:33 | +10 stop | BTC | UP | 0.58 | 0.72 | 1.07 |
| 11-08 01:33 | +10 stop | BNB | UP | 0.56 | 0.28 | -3.13 |
| 11-08 01:33 | +5 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-08 01:33 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-08 01:33 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-08 01:32 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
| 11-08 01:31 | +10 stop | BTC | UP | 0.67 | 0.52 | -1.84 |
| 11-08 01:31 | +20 | BTC | UP | 0.67 | 0.88 | 1.86 |
| 11-08 01:31 | +15 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 11-08 01:31 | +10 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-08 01:31 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 11-08 01:31 | +10 stop | BNB | DOWN | 0.57 | 0.39 | -2.15 |
| 11-08 01:31 | +20 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 11-08 01:31 | +15 | BNB | DOWN | 0.57 | 0.75 | 1.48 |
