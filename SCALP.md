# Range-Scalp Bot

*Updated Sun Oct 25 18:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33541 | 29269 | 4272 (43) | 3 | $-9386.22 | -4.4% |
| **+10¢** | 25105 | 20160 | 4945 (65) | 5 | $-8303.48 | -5.3% |
| **+15¢** | 20997 | 15675 | 5322 (89) | 5 | $-7445.09 | -5.6% |
| **+20¢** | 18609 | 13037 | 5572 (111) | 6 | $-6544.15 | -5.6% |
| **+10¢ (15¢ stop)** | 41104 | 41042 | 62 (33) | 3 | $-15668.79 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 18:18 | +10 stop | BTC | UP | 0.71 | open |  |
| 10-25 18:18 | +10 | BTC | UP | 0.71 | open |  |
| 10-25 18:18 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-25 18:18 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-25 18:18 | +10 | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-25 18:18 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-25 18:17 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-25 18:17 | +20 | ETH | UP | 0.60 | 0.80 | 1.71 |
| 10-25 18:17 | +15 | ETH | UP | 0.60 | 0.75 | 1.19 |
| 10-25 18:17 | +10 | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-25 18:17 | +5 | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-25 18:17 | +10 stop | NEAR | UP | 0.67 | open |  |
| 10-25 18:17 | +20 | NEAR | UP | 0.67 | open |  |
| 10-25 18:17 | +15 | NEAR | UP | 0.67 | open |  |
| 10-25 18:17 | +10 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-25 18:17 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 10-25 18:17 | +10 stop | HYPE | UP | 0.70 | 0.87 | 1.47 |
| 10-25 18:17 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-25 18:17 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-25 18:17 | +20 | BTC | UP | 0.60 | open |  |
| 10-25 18:17 | +15 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 10-25 18:17 | +10 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-25 18:17 | +5 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-25 18:17 | +10 stop | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-25 18:17 | +20 | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 10-25 18:17 | +15 | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 10-25 18:17 | +10 | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-25 18:17 | +5 | ZEC | UP | 0.64 | 0.70 | 0.28 |
| 10-25 18:16 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-25 18:16 | +20 | DOGE | UP | 0.63 | 0.88 | 2.25 |
| 10-25 18:16 | +15 | DOGE | UP | 0.63 | 0.78 | 1.24 |
| 10-25 18:16 | +10 | DOGE | UP | 0.63 | 0.76 | 1.04 |
| 10-25 18:16 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 10-25 18:15 | +10 stop | HYPE | DOWN | 0.56 | 0.37 | -2.25 |
| 10-25 18:15 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-25 18:15 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-25 18:15 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-25 18:15 | +5 | HYPE | DOWN | 0.56 | open |  |
| 10-25 18:15 | +10 stop | XRP | DOWN | 0.54 | 0.36 | -2.15 |
| 10-25 18:15 | +20 | XRP | DOWN | 0.54 | open |  |
