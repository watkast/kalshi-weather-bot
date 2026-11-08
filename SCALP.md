# Range-Scalp Bot

*Updated Sun Nov 08 03:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51910 | 45263 | 6647 (80) | 3 | $-14391.31 | -4.4% |
| **+10¢** | 38741 | 30988 | 7753 (106) | 4 | $-13413.34 | -5.5% |
| **+15¢** | 32443 | 24088 | 8355 (135) | 5 | $-12303.83 | -6.0% |
| **+20¢** | 28866 | 20108 | 8758 (180) | 4 | $-10821.28 | -6.0% |
| **+10¢ (15¢ stop)** | 63216 | 63113 | 103 (61) | 3 | $-23408.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 03:34 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 11-08 03:34 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-08 03:33 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-08 03:33 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 11-08 03:32 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-08 03:32 | +10 stop | ETH | DOWN | 0.54 | open |  |
| 11-08 03:32 | +10 stop | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-08 03:32 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-08 03:32 | +10 stop | BNB | DOWN | 0.65 | 0.91 | 2.39 |
| 11-08 03:32 | +20 | BNB | DOWN | 0.65 | 0.91 | 2.39 |
| 11-08 03:32 | +15 | BNB | DOWN | 0.65 | 0.91 | 2.39 |
| 11-08 03:32 | +10 | BNB | DOWN | 0.65 | 0.91 | 2.39 |
| 11-08 03:32 | +5 | BNB | DOWN | 0.65 | 0.91 | 2.39 |
| 11-08 03:32 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-08 03:32 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-08 03:32 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-08 03:32 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-08 03:32 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 03:31 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-08 03:31 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-08 03:31 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-08 03:31 | +10 stop | DOGE | UP | 0.56 | 0.41 | -1.85 |
| 11-08 03:31 | +20 | DOGE | UP | 0.56 | open |  |
| 11-08 03:31 | +15 | DOGE | UP | 0.56 | open |  |
| 11-08 03:31 | +10 | DOGE | UP | 0.56 | open |  |
| 11-08 03:31 | +5 | DOGE | UP | 0.56 | 0.63 | 0.35 |
| 11-08 03:31 | +10 stop | HYPE | UP | 0.65 | 0.44 | -2.44 |
| 11-08 03:31 | +20 | HYPE | UP | 0.65 | open |  |
| 11-08 03:31 | +15 | HYPE | UP | 0.65 | open |  |
| 11-08 03:31 | +10 | HYPE | UP | 0.65 | open |  |
| 11-08 03:31 | +5 | HYPE | UP | 0.65 | open |  |
| 11-08 03:31 | +10 stop | ETH | UP | 0.60 | 0.42 | -2.15 |
| 11-08 03:31 | +20 | ETH | UP | 0.60 | open |  |
| 11-08 03:31 | +15 | ETH | UP | 0.60 | open |  |
| 11-08 03:31 | +10 | ETH | UP | 0.60 | open |  |
| 11-08 03:31 | +5 | ETH | UP | 0.60 | open |  |
| 11-08 03:31 | +10 stop | DOGE | DOWN | 0.38 | 0.61 | 1.96 |
| 11-08 03:31 | +20 | DOGE | DOWN | 0.38 | 0.61 | 1.96 |
| 11-08 03:31 | +15 | DOGE | DOWN | 0.38 | 0.61 | 1.96 |
| 11-08 03:31 | +10 | DOGE | DOWN | 0.38 | 0.61 | 1.96 |
