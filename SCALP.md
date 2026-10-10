# Range-Scalp Bot

*Updated Sat Oct 10 03:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9884 | 8530 | 1354 (18) | 4 | $-3334.76 | -5.3% |
| **+10¢** | 7468 | 5888 | 1580 (30) | 5 | $-3207.72 | -6.8% |
| **+15¢** | 6301 | 4635 | 1666 (43) | 5 | $-2657.36 | -6.7% |
| **+20¢** | 5600 | 3869 | 1731 (55) | 7 | $-2227.08 | -6.3% |
| **+10¢ (15¢ stop)** | 12138 | 12103 | 35 (22) | 3 | $-4746.45 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 03:19 | +5 | BTC | UP | 0.57 | open |  |
| 10-10 03:19 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 10-10 03:19 | +20 | XRP | DOWN | 0.70 | open |  |
| 10-10 03:19 | +15 | XRP | DOWN | 0.70 | open |  |
| 10-10 03:19 | +10 | XRP | DOWN | 0.70 | open |  |
| 10-10 03:19 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-10 03:19 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 10-10 03:19 | +20 | NEAR | DOWN | 0.54 | open |  |
| 10-10 03:19 | +15 | NEAR | DOWN | 0.54 | open |  |
| 10-10 03:19 | +10 | NEAR | DOWN | 0.54 | open |  |
| 10-10 03:19 | +5 | NEAR | DOWN | 0.54 | 0.60 | 0.25 |
| 10-10 03:18 | +5 | HYPE | UP | 0.67 | 0.78 | 0.77 |
| 10-10 03:18 | +10 stop | ETH | DOWN | 0.63 | 0.42 | -2.45 |
| 10-10 03:18 | +10 | ETH | DOWN | 0.63 | open |  |
| 10-10 03:18 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-10 03:17 | +10 stop | SOL | DOWN | 0.68 | 0.47 | -2.44 |
| 10-10 03:17 | +10 stop | ETH | UP | 0.42 | 0.54 | 0.84 |
| 10-10 03:17 | +20 | ETH | UP | 0.42 | open |  |
| 10-10 03:17 | +15 | ETH | UP | 0.42 | 0.57 | 1.14 |
| 10-10 03:17 | +10 | ETH | UP | 0.42 | 0.54 | 0.84 |
| 10-10 03:17 | +5 | ETH | UP | 0.42 | 0.54 | 0.84 |
| 10-10 03:17 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.81 |
| 10-10 03:17 | +20 | ZEC | UP | 0.70 | open |  |
| 10-10 03:17 | +15 | ZEC | UP | 0.70 | open |  |
| 10-10 03:17 | +10 | ZEC | UP | 0.70 | 0.81 | 0.85 |
| 10-10 03:17 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 10-10 03:17 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.05 |
| 10-10 03:17 | +20 | BNB | UP | 0.59 | 0.82 | 1.98 |
| 10-10 03:17 | +15 | BNB | UP | 0.59 | 0.77 | 1.46 |
| 10-10 03:17 | +10 | BNB | UP | 0.59 | 0.73 | 1.05 |
| 10-10 03:17 | +5 | BNB | UP | 0.59 | 0.73 | 1.05 |
| 10-10 03:17 | +10 stop | HYPE | UP | 0.59 | 0.78 | 1.60 |
| 10-10 03:17 | +20 | HYPE | UP | 0.59 | 0.80 | 1.81 |
| 10-10 03:17 | +15 | HYPE | UP | 0.59 | 0.78 | 1.60 |
| 10-10 03:17 | +10 | HYPE | UP | 0.59 | 0.78 | 1.60 |
| 10-10 03:17 | +5 | HYPE | UP | 0.59 | 0.65 | 0.27 |
| 10-10 03:16 | +10 stop | SOL | UP | 0.61 | 0.39 | -2.54 |
| 10-10 03:16 | +20 | SOL | UP | 0.60 | open |  |
| 10-10 03:16 | +15 | SOL | UP | 0.60 | open |  |
| 10-10 03:16 | +10 | SOL | UP | 0.61 | open |  |
