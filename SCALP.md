# Range-Scalp Bot

*Updated Mon Oct 26 10:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34677 | 30277 | 4400 (43) | 0 | $-9595.25 | -4.4% |
| **+10¢** | 25955 | 20867 | 5088 (65) | 1 | $-8398.91 | -5.1% |
| **+15¢** | 21715 | 16236 | 5479 (89) | 1 | $-7513.06 | -5.5% |
| **+20¢** | 19244 | 13500 | 5744 (112) | 3 | $-6622.03 | -5.5% |
| **+10¢ (15¢ stop)** | 42458 | 42396 | 62 (33) | 1 | $-16124.60 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 10:32 | +5 | ZEC | UP | 0.70 | 0.85 | 1.26 |
| 10-26 10:31 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 10-26 10:31 | +20 | BNB | UP | 0.66 | open |  |
| 10-26 10:31 | +15 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-26 10:31 | +10 | BNB | UP | 0.66 | 0.77 | 0.81 |
| 10-26 10:31 | +5 | BNB | UP | 0.66 | 0.75 | 0.60 |
| 10-26 10:31 | +10 stop | ZEC | UP | 0.65 | 0.85 | 1.75 |
| 10-26 10:31 | +20 | ZEC | UP | 0.65 | 0.85 | 1.75 |
| 10-26 10:31 | +15 | ZEC | UP | 0.65 | 0.85 | 1.75 |
| 10-26 10:31 | +10 | ZEC | UP | 0.65 | 0.85 | 1.75 |
| 10-26 10:31 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 10-26 10:31 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-26 10:31 | +20 | BTC | UP | 0.70 | open |  |
| 10-26 10:31 | +15 | BTC | UP | 0.70 | open |  |
| 10-26 10:31 | +10 | BTC | UP | 0.70 | open |  |
| 10-26 10:31 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-26 10:31 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-26 10:31 | +20 | DOGE | UP | 0.63 | open |  |
| 10-26 10:31 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-26 10:31 | +10 | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-26 10:31 | +5 | DOGE | UP | 0.63 | 0.72 | 0.57 |
| 10-26 10:31 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 10-26 10:31 | +20 | HYPE | UP | 0.67 | 0.87 | 1.76 |
| 10-26 10:31 | +15 | HYPE | UP | 0.67 | 0.86 | 1.65 |
| 10-26 10:31 | +10 | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 10-26 10:31 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 10-26 10:24 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-26 10:24 | +10 stop | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-26 10:24 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-26 10:24 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-26 10:24 | +10 | HYPE | DOWN | 0.71 | 0.92 | 1.92 |
| 10-26 10:24 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.91 |
| 10-26 10:24 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-26 10:24 | +15 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-26 10:24 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 10:24 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-26 10:24 | +10 stop | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-26 10:24 | +20 | BTC | DOWN | 0.62 | 0.92 | 2.76 |
| 10-26 10:24 | +15 | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-26 10:24 | +10 | BTC | DOWN | 0.62 | 0.77 | 1.20 |
