# Range-Scalp Bot

*Updated Fri Nov 27 23:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74009 | 64598 | 9411 (171) | 5 | $-19632.09 | -4.2% |
| **+10¢** | 55146 | 44155 | 10991 (216) | 5 | $-18245.15 | -5.3% |
| **+15¢** | 46175 | 34337 | 11838 (274) | 6 | $-16309.47 | -5.6% |
| **+20¢** | 41093 | 28624 | 12469 (341) | 7 | $-14724.09 | -5.7% |
| **+10¢ (15¢ stop)** | 90106 | 89887 | 219 (135) | 4 | $-33315.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 23:19 | +10 stop | BTC | UP | 0.63 | 0.45 | -2.15 |
| 11-27 23:19 | +10 stop | XRP | UP | 0.58 | open |  |
| 11-27 23:18 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 11-27 23:18 | +20 | DOGE | UP | 0.64 | open |  |
| 11-27 23:18 | +15 | DOGE | UP | 0.65 | open |  |
| 11-27 23:18 | +10 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 11-27 23:18 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 11-27 23:17 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-27 23:17 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 11-27 23:17 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-27 23:17 | +15 | SOL | DOWN | 0.69 | open |  |
| 11-27 23:17 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-27 23:17 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-27 23:16 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-27 23:16 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:16 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:16 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:16 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:16 | +10 stop | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 11-27 23:16 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.71 |
| 11-27 23:16 | +15 | NEAR | DOWN | 0.59 | 0.79 | 1.72 |
| 11-27 23:16 | +10 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-27 23:16 | +5 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-27 23:16 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-27 23:16 | +20 | ZEC | DOWN | 0.70 | open |  |
| 11-27 23:16 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-27 23:16 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-27 23:16 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-27 23:16 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 11-27 23:16 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-27 23:16 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-27 23:16 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-27 23:16 | +5 | BTC | DOWN | 0.63 | open |  |
| 11-27 23:15 | +10 stop | ETH | DOWN | 0.64 | open |  |
| 11-27 23:15 | +20 | ETH | DOWN | 0.64 | open |  |
| 11-27 23:15 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-27 23:15 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-27 23:15 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 11-27 23:15 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 11-27 23:15 | +20 | XRP | DOWN | 0.65 | open |  |
