# Range-Scalp Bot

*Updated Wed Nov 25 03:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71312 | 62246 | 9066 (156) | 4 | $-18990.08 | -4.2% |
| **+10¢** | 53190 | 42601 | 10589 (202) | 5 | $-17589.74 | -5.3% |
| **+15¢** | 44547 | 33147 | 11400 (259) | 6 | $-15632.24 | -5.6% |
| **+20¢** | 39658 | 27655 | 12003 (325) | 8 | $-14020.01 | -5.6% |
| **+10¢ (15¢ stop)** | 86830 | 86627 | 203 (123) | 0 | $-31903.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 03:09 | +10 stop | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 11-25 03:09 | +5 | SOL | UP | 0.71 | 0.83 | 1.00 |
| 11-25 03:09 | +10 stop | BNB | UP | 0.68 | 0.80 | 0.92 |
| 11-25 03:09 | +10 stop | XRP | UP | 0.43 | 0.55 | 0.84 |
| 11-25 03:09 | +20 | XRP | UP | 0.43 | 0.72 | 2.57 |
| 11-25 03:09 | +15 | XRP | UP | 0.44 | 0.72 | 2.47 |
| 11-25 03:09 | +10 | XRP | UP | 0.44 | 0.55 | 0.74 |
| 11-25 03:09 | +5 | XRP | UP | 0.44 | 0.55 | 0.74 |
| 11-25 03:08 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
| 11-25 03:08 | +15 | BTC | UP | 0.64 | 0.83 | 1.63 |
| 11-25 03:08 | +10 | BTC | UP | 0.64 | 0.75 | 0.79 |
| 11-25 03:08 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-25 03:07 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-25 03:07 | +15 | SOL | UP | 0.59 | 0.83 | 2.13 |
| 11-25 03:07 | +10 | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-25 03:07 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 11-25 03:07 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-25 03:07 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-25 03:07 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-25 03:07 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-25 03:07 | +5 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-25 03:07 | +10 stop | ZEC | UP | 0.57 | 0.69 | 0.89 |
| 11-25 03:07 | +10 stop | NEAR | UP | 0.60 | 0.78 | 1.50 |
| 11-25 03:07 | +5 | HYPE | DOWN | 0.53 | open |  |
| 11-25 03:07 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.76 |
| 11-25 03:07 | +10 stop | ETH | UP | 0.60 | 0.70 | 0.68 |
| 11-25 03:07 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 11-25 03:06 | +10 stop | SOL | DOWN | 0.46 | 0.64 | 1.45 |
| 11-25 03:06 | +20 | SOL | DOWN | 0.46 | open |  |
| 11-25 03:06 | +15 | SOL | DOWN | 0.46 | 0.64 | 1.45 |
| 11-25 03:06 | +10 | SOL | DOWN | 0.46 | 0.64 | 1.45 |
| 11-25 03:06 | +5 | SOL | DOWN | 0.46 | 0.64 | 1.45 |
| 11-25 03:06 | +10 stop | HYPE | DOWN | 0.52 | 0.34 | -2.19 |
| 11-25 03:06 | +15 | HYPE | DOWN | 0.52 | open |  |
| 11-25 03:06 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-25 03:06 | +5 | HYPE | DOWN | 0.50 | 0.59 | 0.55 |
| 11-25 03:06 | +10 stop | BNB | DOWN | 0.62 | 0.38 | -2.74 |
| 11-25 03:06 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-25 03:06 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-25 03:06 | +5 | BNB | DOWN | 0.62 | open |  |
