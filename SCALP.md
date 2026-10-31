# Range-Scalp Bot

*Updated Sat Oct 31 21:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42727 | 37254 | 5473 (62) | 3 | $-12076.08 | -4.5% |
| **+10¢** | 31858 | 25528 | 6330 (84) | 4 | $-10839.53 | -5.4% |
| **+15¢** | 26653 | 19826 | 6827 (112) | 4 | $-9943.13 | -5.9% |
| **+20¢** | 23671 | 16516 | 7155 (144) | 4 | $-8827.05 | -5.9% |
| **+10¢ (15¢ stop)** | 52127 | 52044 | 83 (48) | 0 | $-19732.61 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 20:58 | +10 stop | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 10-31 20:56 | +10 stop | NEAR | UP | 0.71 | 0.44 | -3.03 |
| 10-31 20:56 | +15 | NEAR | UP | 0.71 | open |  |
| 10-31 20:56 | +10 | NEAR | UP | 0.71 | open |  |
| 10-31 20:56 | +5 | NEAR | UP | 0.71 | open |  |
| 10-31 20:55 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-31 20:55 | +10 stop | ZEC | UP | 0.53 | 0.37 | -1.95 |
| 10-31 20:55 | +15 | ZEC | UP | 0.53 | open |  |
| 10-31 20:55 | +10 | ZEC | UP | 0.53 | open |  |
| 10-31 20:55 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 10-31 20:55 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-31 20:54 | +10 stop | NEAR | UP | 0.62 | 0.73 | 0.79 |
| 10-31 20:54 | +10 | NEAR | UP | 0.62 | 0.73 | 0.79 |
| 10-31 20:53 | +20 | DOGE | DOWN | 0.69 | 0.97 | 2.59 |
| 10-31 20:53 | +5 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-31 20:53 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.84 |
| 10-31 20:53 | +5 | ZEC | UP | 0.63 | 0.72 | 0.58 |
| 10-31 20:52 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 10-31 20:52 | +10 | SOL | UP | 0.61 | 0.72 | 0.78 |
| 10-31 20:52 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 10-31 20:52 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 10-31 20:51 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-31 20:51 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-31 20:51 | +15 | DOGE | DOWN | 0.68 | 0.97 | 2.68 |
| 10-31 20:51 | +10 | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-31 20:51 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-31 20:51 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-31 20:51 | +10 stop | XRP | DOWN | 0.54 | 0.39 | -1.85 |
| 10-31 20:51 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-31 20:51 | +20 | SOL | UP | 0.56 | 0.77 | 1.79 |
| 10-31 20:51 | +15 | SOL | UP | 0.56 | 0.72 | 1.27 |
| 10-31 20:51 | +10 | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-31 20:51 | +5 | SOL | UP | 0.56 | 0.63 | 0.35 |
| 10-31 20:50 | +5 | ZEC | UP | 0.56 | 0.62 | 0.25 |
| 10-31 20:49 | +10 stop | XRP | UP | 0.64 | 0.45 | -2.25 |
| 10-31 20:49 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 10-31 20:48 | +5 | ETH | UP | 0.71 | 0.76 | 0.22 |
| 10-31 20:48 | +10 stop | SOL | UP | 0.65 | 0.87 | 1.96 |
| 10-31 20:48 | +20 | SOL | UP | 0.65 | 0.87 | 1.96 |
| 10-31 20:48 | +15 | SOL | UP | 0.65 | 0.87 | 1.96 |
