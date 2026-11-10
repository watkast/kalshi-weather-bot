# Range-Scalp Bot

*Updated Tue Nov 10 18:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54863 | 47852 | 7011 (91) | 1 | $-14975.16 | -4.3% |
| **+10¢** | 40994 | 32815 | 8179 (121) | 2 | $-13888.53 | -5.4% |
| **+15¢** | 34366 | 25552 | 8814 (155) | 3 | $-12615.96 | -5.9% |
| **+20¢** | 30593 | 21345 | 9248 (204) | 6 | $-11044.89 | -5.8% |
| **+10¢ (15¢ stop)** | 66847 | 66733 | 114 (70) | 2 | $-24736.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 18:18 | +5 | ZEC | UP | 0.68 | open |  |
| 11-10 18:16 | +10 stop | BTC | UP | 0.68 | open |  |
| 11-10 18:16 | +20 | BTC | UP | 0.68 | open |  |
| 11-10 18:16 | +15 | BTC | UP | 0.68 | open |  |
| 11-10 18:16 | +10 | BTC | UP | 0.68 | open |  |
| 11-10 18:16 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 11-10 18:16 | +10 stop | HYPE | UP | 0.64 | 0.84 | 1.70 |
| 11-10 18:16 | +20 | HYPE | UP | 0.64 | open |  |
| 11-10 18:16 | +15 | HYPE | UP | 0.64 | 0.84 | 1.70 |
| 11-10 18:16 | +10 | HYPE | UP | 0.64 | 0.84 | 1.70 |
| 11-10 18:16 | +5 | HYPE | UP | 0.64 | 0.72 | 0.45 |
| 11-10 18:16 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-10 18:16 | +20 | XRP | UP | 0.63 | open |  |
| 11-10 18:16 | +15 | XRP | UP | 0.63 | open |  |
| 11-10 18:16 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-10 18:16 | +5 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-10 18:16 | +10 stop | ZEC | UP | 0.62 | open |  |
| 11-10 18:16 | +20 | ZEC | UP | 0.62 | open |  |
| 11-10 18:16 | +15 | ZEC | UP | 0.62 | open |  |
| 11-10 18:16 | +10 | ZEC | UP | 0.62 | open |  |
| 11-10 18:16 | +5 | ZEC | UP | 0.63 | 0.70 | 0.38 |
| 11-10 18:16 | +10 stop | BNB | UP | 0.63 | 0.76 | 0.96 |
| 11-10 18:16 | +20 | BNB | UP | 0.64 | open |  |
| 11-10 18:16 | +15 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-10 18:16 | +10 | BNB | UP | 0.63 | 0.76 | 1.00 |
| 11-10 18:16 | +5 | BNB | UP | 0.63 | 0.70 | 0.38 |
| 11-10 18:16 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-10 18:16 | +20 | ETH | UP | 0.68 | open |  |
| 11-10 18:16 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 11-10 18:16 | +10 | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-10 18:16 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 11-10 18:12 | +10 stop | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-10 18:11 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.70 |
| 11-10 18:11 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-10 18:11 | +15 | SOL | UP | 0.66 | no | -6.76 |
| 11-10 18:10 | +10 | SOL | UP | 0.70 | no | -7.15 |
| 11-10 18:10 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-10 18:10 | +5 | SOL | UP | 0.63 | 0.70 | 0.40 |
| 11-10 18:10 | +10 stop | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 11-10 18:10 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
