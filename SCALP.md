# Range-Scalp Bot

*Updated Sat Oct 17 13:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20992 | 18266 | 2726 (29) | 5 | $-6144.36 | -4.6% |
| **+10¢** | 15802 | 12658 | 3144 (41) | 5 | $-5467.30 | -5.5% |
| **+15¢** | 13210 | 9826 | 3384 (61) | 5 | $-4946.64 | -6.0% |
| **+20¢** | 11709 | 8164 | 3545 (80) | 7 | $-4385.93 | -6.0% |
| **+10¢ (15¢ stop)** | 25787 | 25737 | 50 (29) | 4 | $-9811.18 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 13:03 | +5 | BTC | UP | 0.70 | open |  |
| 10-17 13:03 | +5 | ETH | UP | 0.58 | open |  |
| 10-17 13:03 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 10-17 13:03 | +10 stop | NEAR | UP | 0.58 | open |  |
| 10-17 13:02 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-17 13:02 | +10 stop | ETH | UP | 0.65 | open |  |
| 10-17 13:02 | +20 | ETH | UP | 0.65 | open |  |
| 10-17 13:02 | +15 | ETH | UP | 0.65 | open |  |
| 10-17 13:02 | +10 | ETH | UP | 0.65 | open |  |
| 10-17 13:02 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 10-17 13:02 | +10 stop | ZEC | DOWN | 0.62 | 0.38 | -2.74 |
| 10-17 13:02 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-17 13:02 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-17 13:02 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-17 13:02 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-17 13:01 | +10 stop | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-17 13:01 | +20 | SOL | UP | 0.69 | open |  |
| 10-17 13:01 | +15 | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-17 13:01 | +10 | SOL | UP | 0.69 | 0.83 | 1.15 |
| 10-17 13:01 | +5 | SOL | UP | 0.69 | 0.75 | 0.31 |
| 10-17 13:01 | +10 stop | NEAR | DOWN | 0.51 | 0.35 | -1.94 |
| 10-17 13:01 | +20 | NEAR | DOWN | 0.52 | open |  |
| 10-17 13:01 | +15 | NEAR | DOWN | 0.52 | open |  |
| 10-17 13:01 | +10 | NEAR | DOWN | 0.52 | open |  |
| 10-17 13:01 | +5 | NEAR | DOWN | 0.52 | open |  |
| 10-17 13:01 | +10 stop | BTC | UP | 0.66 | open |  |
| 10-17 13:01 | +20 | BTC | UP | 0.66 | open |  |
| 10-17 13:01 | +15 | BTC | UP | 0.66 | open |  |
| 10-17 13:01 | +10 | BTC | UP | 0.66 | open |  |
| 10-17 13:01 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-17 13:01 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-17 13:01 | +20 | DOGE | UP | 0.65 | open |  |
| 10-17 13:01 | +15 | DOGE | UP | 0.65 | 0.83 | 1.54 |
| 10-17 13:01 | +10 | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-17 13:01 | +5 | DOGE | UP | 0.65 | 0.71 | 0.29 |
| 10-17 13:01 | +10 stop | XRP | UP | 0.62 | 0.79 | 1.41 |
| 10-17 13:01 | +20 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-17 13:01 | +15 | XRP | UP | 0.62 | 0.79 | 1.41 |
| 10-17 13:01 | +10 | XRP | UP | 0.62 | 0.79 | 1.41 |
| 10-17 13:01 | +5 | XRP | UP | 0.62 | 0.71 | 0.58 |
