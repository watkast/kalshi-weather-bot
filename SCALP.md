# Range-Scalp Bot

*Updated Tue Nov 10 13:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54537 | 47570 | 6967 (91) | 3 | $-14864.82 | -4.3% |
| **+10¢** | 40745 | 32613 | 8132 (121) | 4 | $-13815.67 | -5.4% |
| **+15¢** | 34154 | 25386 | 8768 (155) | 4 | $-12587.42 | -5.9% |
| **+20¢** | 30414 | 21217 | 9197 (204) | 4 | $-10985.37 | -5.8% |
| **+10¢ (15¢ stop)** | 66454 | 66340 | 114 (70) | 4 | $-24583.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 13:21 | +10 stop | HYPE | UP | 0.60 | open |  |
| 11-10 13:21 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-10 13:21 | +10 stop | NEAR | DOWN | 0.53 | open |  |
| 11-10 13:21 | +20 | NEAR | DOWN | 0.53 | open |  |
| 11-10 13:21 | +15 | NEAR | DOWN | 0.53 | open |  |
| 11-10 13:21 | +10 | NEAR | DOWN | 0.53 | open |  |
| 11-10 13:21 | +5 | NEAR | DOWN | 0.53 | 0.60 | 0.35 |
| 11-10 13:21 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-10 13:20 | +10 stop | BNB | DOWN | 0.71 | 0.53 | -2.13 |
| 11-10 13:20 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-10 13:20 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-10 13:20 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-10 13:20 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-10 13:20 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 11-10 13:20 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-10 13:20 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-10 13:20 | +10 | ZEC | DOWN | 0.66 | open |  |
| 11-10 13:20 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-10 13:19 | +10 stop | HYPE | DOWN | 0.66 | 0.37 | -3.23 |
| 11-10 13:19 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-10 13:19 | +15 | HYPE | DOWN | 0.66 | open |  |
| 11-10 13:19 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-10 13:19 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-10 13:15 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 13:15 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-10 13:15 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-10 13:15 | +10 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-10 13:15 | +5 | XRP | DOWN | 0.67 | 0.76 | 0.61 |
| 11-10 13:14 | +10 stop | ZEC | UP | 0.09 | 0.53 | 4.12 |
| 11-10 13:12 | +10 stop | ETH | DOWN | 0.60 | 0.33 | -3.03 |
| 11-10 13:12 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.27 |
| 11-10 13:12 | +5 | ZEC | DOWN | 0.53 | 0.91 | 3.50 |
| 11-10 13:12 | +10 stop | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 11-10 13:12 | +10 | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 11-10 13:12 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-10 13:11 | +10 stop | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-10 13:11 | +10 stop | ZEC | DOWN | 0.56 | 0.17 | -4.17 |
| 11-10 13:11 | +5 | ZEC | DOWN | 0.53 | 0.63 | 0.69 |
| 11-10 13:11 | +10 stop | BTC | DOWN | 0.61 | 0.41 | -2.34 |
| 11-10 13:11 | +10 stop | BNB | UP | 0.65 | 0.75 | 0.70 |
