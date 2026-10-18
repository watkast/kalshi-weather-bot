# Range-Scalp Bot

*Updated Sun Oct 18 12:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22583 | 19659 | 2924 (29) | 4 | $-6590.31 | -4.6% |
| **+10¢** | 16987 | 13609 | 3378 (43) | 6 | $-5867.87 | -5.5% |
| **+15¢** | 14223 | 10577 | 3646 (64) | 6 | $-5366.08 | -6.0% |
| **+20¢** | 12590 | 8773 | 3817 (82) | 6 | $-4781.67 | -6.1% |
| **+10¢ (15¢ stop)** | 27769 | 27719 | 50 (29) | 1 | $-10603.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 12:52 | +10 stop | SOL | UP | 0.42 | 0.54 | 0.84 |
| 10-18 12:52 | +5 | SOL | UP | 0.44 | 0.54 | 0.64 |
| 10-18 12:51 | +10 stop | ZEC | UP | 0.70 | open |  |
| 10-18 12:51 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.05 |
| 10-18 12:51 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-18 12:51 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-18 12:51 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-18 12:51 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-18 12:51 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-18 12:51 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.85 |
| 10-18 12:51 | +20 | XRP | DOWN | 0.59 | open |  |
| 10-18 12:51 | +15 | XRP | DOWN | 0.59 | open |  |
| 10-18 12:51 | +10 | XRP | DOWN | 0.59 | open |  |
| 10-18 12:51 | +5 | XRP | DOWN | 0.59 | open |  |
| 10-18 12:50 | +10 stop | BTC | DOWN | 0.43 | 0.56 | 0.94 |
| 10-18 12:50 | +10 stop | BTC | UP | 0.52 | 0.62 | 0.65 |
| 10-18 12:49 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 10-18 12:48 | +10 stop | SOL | DOWN | 0.64 | 0.33 | -3.43 |
| 10-18 12:48 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-18 12:48 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-18 12:47 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-18 12:47 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-18 12:47 | +10 stop | ETH | DOWN | 0.65 | 0.29 | -3.91 |
| 10-18 12:47 | +10 stop | ZEC | DOWN | 0.63 | 0.41 | -2.54 |
| 10-18 12:47 | +20 | ZEC | DOWN | 0.63 | open |  |
| 10-18 12:47 | +15 | ZEC | DOWN | 0.63 | open |  |
| 10-18 12:47 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-18 12:47 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-18 12:47 | +10 stop | NEAR | DOWN | 0.53 | 0.32 | -2.44 |
| 10-18 12:47 | +20 | NEAR | DOWN | 0.53 | open |  |
| 10-18 12:47 | +15 | NEAR | DOWN | 0.53 | open |  |
| 10-18 12:47 | +10 | NEAR | DOWN | 0.53 | open |  |
| 10-18 12:47 | +5 | NEAR | DOWN | 0.53 | 0.60 | 0.35 |
| 10-18 12:46 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-18 12:46 | +20 | DOGE | DOWN | 0.68 | 0.91 | 2.09 |
| 10-18 12:46 | +15 | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-18 12:46 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-18 12:46 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-18 12:46 | +10 stop | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 10-18 12:46 | +20 | XRP | DOWN | 0.60 | 0.81 | 1.82 |
