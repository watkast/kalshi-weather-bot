# Range-Scalp Bot

*Updated Sun Nov 08 10:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52336 | 45627 | 6709 (82) | 4 | $-14534.88 | -4.4% |
| **+10¢** | 39065 | 31245 | 7820 (107) | 4 | $-13540.36 | -5.5% |
| **+15¢** | 32724 | 24296 | 8428 (137) | 5 | $-12408.55 | -6.0% |
| **+20¢** | 29106 | 20273 | 8833 (181) | 6 | $-10924.90 | -6.0% |
| **+10¢ (15¢ stop)** | 63713 | 63608 | 105 (62) | 2 | $-23555.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 10:37 | +5 | BNB | UP | 0.60 | open |  |
| 11-08 10:37 | +10 stop | BNB | UP | 0.61 | open |  |
| 11-08 10:37 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-08 10:35 | +10 stop | BNB | UP | 0.58 | 0.43 | -1.86 |
| 11-08 10:35 | +20 | BNB | UP | 0.58 | open |  |
| 11-08 10:35 | +15 | BNB | UP | 0.58 | open |  |
| 11-08 10:35 | +10 | BNB | UP | 0.58 | open |  |
| 11-08 10:35 | +5 | BNB | UP | 0.58 | 0.64 | 0.25 |
| 11-08 10:34 | +10 stop | XRP | UP | 0.64 | 0.35 | -3.18 |
| 11-08 10:34 | +5 | XRP | UP | 0.64 | open |  |
| 11-08 10:34 | +10 stop | ZEC | DOWN | 0.59 | 0.40 | -2.24 |
| 11-08 10:34 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-08 10:34 | +15 | ZEC | DOWN | 0.59 | open |  |
| 11-08 10:34 | +10 | ZEC | DOWN | 0.59 | open |  |
| 11-08 10:34 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-08 10:34 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-08 10:34 | +5 | SOL | DOWN | 0.59 | 0.68 | 0.57 |
| 11-08 10:34 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.85 |
| 11-08 10:34 | +20 | NEAR | DOWN | 0.63 | 0.86 | 2.00 |
| 11-08 10:34 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.27 |
| 11-08 10:34 | +10 | NEAR | DOWN | 0.63 | 0.75 | 0.85 |
| 11-08 10:34 | +5 | NEAR | DOWN | 0.63 | 0.75 | 0.85 |
| 11-08 10:34 | +10 stop | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-08 10:34 | +20 | HYPE | DOWN | 0.55 | 0.82 | 2.41 |
| 11-08 10:34 | +15 | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 11-08 10:34 | +10 | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-08 10:34 | +5 | HYPE | DOWN | 0.55 | 0.61 | 0.25 |
| 11-08 10:34 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-08 10:33 | +5 | XRP | DOWN | 0.45 | 0.56 | 0.74 |
| 11-08 10:33 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-08 10:33 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-08 10:33 | +5 | ETH | DOWN | 0.58 | 0.67 | 0.56 |
| 11-08 10:33 | +10 stop | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 11-08 10:33 | +15 | SOL | DOWN | 0.56 | 0.77 | 1.79 |
| 11-08 10:33 | +10 | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 11-08 10:33 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 11-08 10:32 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 11-08 10:32 | +20 | ETH | DOWN | 0.66 | open |  |
| 11-08 10:32 | +15 | ETH | DOWN | 0.66 | open |  |
| 11-08 10:32 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
