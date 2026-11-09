# Range-Scalp Bot

*Updated Mon Nov 09 04:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53264 | 46444 | 6820 (85) | 4 | $-14702.64 | -4.4% |
| **+10¢** | 39779 | 31824 | 7955 (110) | 3 | $-13699.71 | -5.5% |
| **+15¢** | 33331 | 24760 | 8571 (141) | 3 | $-12508.61 | -6.0% |
| **+20¢** | 29652 | 20665 | 8987 (186) | 3 | $-11009.64 | -5.9% |
| **+10¢ (15¢ stop)** | 64903 | 64797 | 106 (63) | 0 | $-24086.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 04:08 | +5 | HYPE | UP | 0.43 | 0.61 | 1.45 |
| 11-09 04:07 | +10 stop | HYPE | UP | 0.62 | 0.80 | 1.54 |
| 11-09 04:07 | +10 stop | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-09 04:07 | +10 | ZEC | DOWN | 0.53 | 0.68 | 1.16 |
| 11-09 04:07 | +5 | ZEC | DOWN | 0.53 | 0.61 | 0.45 |
| 11-09 04:06 | +10 stop | ZEC | DOWN | 0.52 | 0.63 | 0.77 |
| 11-09 04:06 | +20 | ZEC | DOWN | 0.52 | 0.73 | 1.80 |
| 11-09 04:06 | +15 | ZEC | DOWN | 0.51 | 0.68 | 1.36 |
| 11-09 04:06 | +10 | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-09 04:06 | +5 | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-09 04:06 | +10 stop | HYPE | DOWN | 0.66 | 0.45 | -2.44 |
| 11-09 04:06 | +10 stop | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 11-09 04:06 | +10 stop | SOL | UP | 0.65 | 0.83 | 1.54 |
| 11-09 04:06 | +10 stop | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-09 04:06 | +10 stop | ETH | UP | 0.55 | 0.65 | 0.66 |
| 11-09 04:05 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-09 04:04 | +10 stop | BNB | DOWN | 0.61 | 0.46 | -1.85 |
| 11-09 04:04 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-09 04:04 | +10 stop | NEAR | DOWN | 0.56 | 0.41 | -1.85 |
| 11-09 04:04 | +10 stop | DOGE | DOWN | 0.62 | 0.35 | -3.01 |
| 11-09 04:04 | +5 | DOGE | DOWN | 0.67 | open |  |
| 11-09 04:04 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-09 04:03 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-09 04:03 | +10 stop | SOL | DOWN | 0.63 | 0.40 | -2.64 |
| 11-09 04:03 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-09 04:03 | +15 | SOL | DOWN | 0.63 | open |  |
| 11-09 04:03 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-09 04:03 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-09 04:03 | +10 stop | ETH | DOWN | 0.60 | 0.45 | -1.85 |
| 11-09 04:03 | +10 stop | BTC | DOWN | 0.55 | 0.34 | -2.44 |
| 11-09 04:03 | +5 | DOGE | UP | 0.40 | 0.56 | 1.25 |
| 11-09 04:02 | +5 | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-09 04:02 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 11-09 04:02 | +20 | XRP | UP | 0.70 | 0.92 | 1.94 |
| 11-09 04:02 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-09 04:02 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-09 04:02 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 11-09 04:02 | +5 | HYPE | UP | 0.53 | 0.64 | 0.75 |
| 11-09 04:02 | +10 stop | BNB | DOWN | 0.52 | 0.65 | 0.96 |
| 11-09 04:02 | +20 | BNB | DOWN | 0.52 | open |  |
