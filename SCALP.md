# Range-Scalp Bot

*Updated Tue Oct 20 03:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25034 | 21796 | 3238 (31) | 3 | $-7319.14 | -4.6% |
| **+10¢** | 18827 | 15088 | 3739 (46) | 7 | $-6489.60 | -5.5% |
| **+15¢** | 15756 | 11729 | 4027 (70) | 7 | $-5846.12 | -5.9% |
| **+20¢** | 13931 | 9715 | 4216 (88) | 7 | $-5246.55 | -6.0% |
| **+10¢ (15¢ stop)** | 30719 | 30667 | 52 (30) | 0 | $-11431.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 03:33 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-20 03:32 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-20 03:32 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-20 03:32 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 10-20 03:32 | +5 | ZEC | UP | 0.66 | 0.72 | 0.26 |
| 10-20 03:32 | +5 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-20 03:32 | +10 stop | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-20 03:32 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-20 03:32 | +20 | XRP | UP | 0.70 | 0.92 | 1.96 |
| 10-20 03:32 | +15 | XRP | UP | 0.70 | 0.87 | 1.47 |
| 10-20 03:32 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-20 03:32 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-20 03:31 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-20 03:31 | +10 stop | BNB | DOWN | 0.54 | 0.39 | -1.85 |
| 10-20 03:31 | +20 | BNB | DOWN | 0.54 | open |  |
| 10-20 03:31 | +15 | BNB | DOWN | 0.54 | open |  |
| 10-20 03:31 | +10 | BNB | DOWN | 0.54 | open |  |
| 10-20 03:31 | +5 | BNB | DOWN | 0.54 | open |  |
| 10-20 03:31 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 10-20 03:31 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-20 03:31 | +15 | BTC | DOWN | 0.56 | open |  |
| 10-20 03:31 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-20 03:31 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-20 03:31 | +10 stop | ZEC | DOWN | 0.54 | 0.36 | -2.15 |
| 10-20 03:31 | +20 | ZEC | DOWN | 0.54 | open |  |
| 10-20 03:31 | +15 | ZEC | DOWN | 0.54 | open |  |
| 10-20 03:31 | +10 | ZEC | DOWN | 0.55 | open |  |
| 10-20 03:31 | +5 | ZEC | DOWN | 0.55 | 0.61 | 0.25 |
| 10-20 03:31 | +10 stop | HYPE | DOWN | 0.52 | 0.36 | -1.95 |
| 10-20 03:31 | +20 | HYPE | DOWN | 0.52 | open |  |
| 10-20 03:31 | +15 | HYPE | DOWN | 0.52 | open |  |
| 10-20 03:31 | +10 | HYPE | DOWN | 0.52 | open |  |
| 10-20 03:31 | +5 | HYPE | DOWN | 0.52 | 0.57 | 0.14 |
| 10-20 03:31 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.05 |
| 10-20 03:31 | +20 | SOL | DOWN | 0.62 | open |  |
| 10-20 03:31 | +15 | SOL | DOWN | 0.62 | open |  |
| 10-20 03:31 | +10 | SOL | DOWN | 0.62 | open |  |
| 10-20 03:31 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-20 03:31 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-20 03:31 | +20 | DOGE | DOWN | 0.59 | open |  |
