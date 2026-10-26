# Range-Scalp Bot

*Updated Mon Oct 26 06:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34361 | 29994 | 4367 (43) | 6 | $-9544.51 | -4.4% |
| **+10¢** | 25722 | 20671 | 5051 (65) | 6 | $-8384.05 | -5.2% |
| **+15¢** | 21511 | 16076 | 5435 (89) | 7 | $-7485.29 | -5.5% |
| **+20¢** | 19062 | 13367 | 5695 (112) | 8 | $-6591.55 | -5.5% |
| **+10¢ (15¢ stop)** | 42107 | 42045 | 62 (33) | 0 | $-16045.77 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 06:04 | +10 stop | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-26 06:04 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-26 06:04 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-26 06:03 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-26 06:03 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-26 06:02 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 10-26 06:02 | +10 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 10-26 06:02 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 10-26 06:02 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-26 06:02 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 10-26 06:02 | +15 | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 10-26 06:02 | +10 | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 10-26 06:02 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.25 |
| 10-26 06:02 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-26 06:02 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-26 06:02 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 06:02 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-26 06:02 | +10 stop | BNB | UP | 0.63 | 0.46 | -2.05 |
| 10-26 06:02 | +20 | BNB | UP | 0.63 | open |  |
| 10-26 06:02 | +15 | BNB | UP | 0.63 | open |  |
| 10-26 06:02 | +10 | BNB | UP | 0.63 | open |  |
| 10-26 06:02 | +5 | BNB | UP | 0.63 | open |  |
| 10-26 06:01 | +10 stop | NEAR | UP | 0.70 | 0.43 | -3.03 |
| 10-26 06:01 | +20 | NEAR | UP | 0.70 | open |  |
| 10-26 06:01 | +15 | NEAR | UP | 0.70 | open |  |
| 10-26 06:01 | +10 | NEAR | UP | 0.70 | open |  |
| 10-26 06:01 | +5 | NEAR | UP | 0.70 | open |  |
| 10-26 06:01 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 10-26 06:01 | +20 | ETH | UP | 0.67 | open |  |
| 10-26 06:01 | +15 | ETH | UP | 0.67 | open |  |
| 10-26 06:01 | +10 | ETH | UP | 0.67 | open |  |
| 10-26 06:01 | +5 | ETH | UP | 0.67 | open |  |
| 10-26 06:01 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 10-26 06:01 | +20 | ZEC | UP | 0.62 | open |  |
| 10-26 06:01 | +15 | ZEC | UP | 0.62 | open |  |
| 10-26 06:01 | +10 | ZEC | UP | 0.62 | open |  |
| 10-26 06:01 | +5 | ZEC | UP | 0.61 | open |  |
| 10-26 06:01 | +10 stop | DOGE | UP | 0.61 | 0.45 | -1.95 |
| 10-26 06:01 | +20 | DOGE | UP | 0.61 | open |  |
| 10-26 06:01 | +15 | DOGE | UP | 0.61 | open |  |
