# Range-Scalp Bot

*Updated Mon Nov 09 01:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53138 | 46340 | 6798 (85) | 5 | $-14631.25 | -4.4% |
| **+10¢** | 39674 | 31744 | 7930 (110) | 6 | $-13631.30 | -5.5% |
| **+15¢** | 33242 | 24700 | 8542 (141) | 7 | $-12424.06 | -6.0% |
| **+20¢** | 29566 | 20609 | 8957 (186) | 9 | $-10942.64 | -5.9% |
| **+10¢ (15¢ stop)** | 64720 | 64614 | 106 (63) | 2 | $-23970.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 01:55 | +10 stop | BTC | DOWN | 0.51 | 0.33 | -2.14 |
| 11-09 01:54 | +10 stop | XRP | UP | 0.69 | 0.84 | 1.25 |
| 11-09 01:54 | +20 | XRP | UP | 0.69 | open |  |
| 11-09 01:54 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 11-09 01:54 | +10 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 11-09 01:54 | +5 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 11-09 01:54 | +10 stop | SOL | DOWN | 0.56 | open |  |
| 11-09 01:54 | +10 stop | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 11-09 01:54 | +20 | DOGE | UP | 0.64 | open |  |
| 11-09 01:54 | +15 | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 11-09 01:54 | +10 | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 11-09 01:54 | +5 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 11-09 01:54 | +10 stop | BNB | UP | 0.64 | open |  |
| 11-09 01:54 | +20 | BNB | UP | 0.64 | open |  |
| 11-09 01:54 | +15 | BNB | UP | 0.64 | open |  |
| 11-09 01:54 | +10 | BNB | UP | 0.64 | open |  |
| 11-09 01:54 | +5 | BNB | UP | 0.64 | 0.72 | 0.48 |
| 11-09 01:54 | +10 stop | HYPE | UP | 0.66 | 0.86 | 1.75 |
| 11-09 01:54 | +10 stop | ZEC | DOWN | 0.69 | 0.41 | -3.12 |
| 11-09 01:53 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 11-09 01:53 | +10 stop | SOL | UP | 0.42 | 0.55 | 0.94 |
| 11-09 01:53 | +10 stop | ETH | UP | 0.50 | 0.60 | 0.65 |
| 11-09 01:51 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 11-09 01:50 | +10 stop | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 11-09 01:50 | +10 | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 11-09 01:50 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 11-09 01:50 | +10 stop | ETH | UP | 0.63 | 0.79 | 1.31 |
| 11-09 01:49 | +10 stop | SOL | DOWN | 0.64 | 0.42 | -2.55 |
| 11-09 01:49 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-09 01:49 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-09 01:49 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-09 01:49 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-09 01:49 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-09 01:49 | +5 | BNB | UP | 0.66 | 0.75 | 0.60 |
| 11-09 01:49 | +10 stop | HYPE | UP | 0.57 | 0.73 | 1.28 |
| 11-09 01:49 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-09 01:49 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-09 01:49 | +10 stop | ZEC | DOWN | 0.61 | 0.38 | -2.64 |
| 11-09 01:49 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-09 01:49 | +5 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
