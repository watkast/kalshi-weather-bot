# Range-Scalp Bot

*Updated Mon Nov 09 04:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53313 | 46487 | 6826 (85) | 8 | $-14710.98 | -4.4% |
| **+10¢** | 39814 | 31852 | 7962 (110) | 9 | $-13712.16 | -5.5% |
| **+15¢** | 33362 | 24783 | 8579 (141) | 9 | $-12517.13 | -6.0% |
| **+20¢** | 29683 | 20688 | 8995 (186) | 9 | $-11012.23 | -5.9% |
| **+10¢ (15¢ stop)** | 64977 | 64871 | 106 (63) | 0 | $-24118.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 04:51 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 04:51 | +5 | DOGE | DOWN | 0.70 | 0.83 | 1.09 |
| 11-09 04:51 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-09 04:51 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.79 |
| 11-09 04:51 | +10 stop | SOL | DOWN | 0.63 | 0.84 | 1.83 |
| 11-09 04:50 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.82 |
| 11-09 04:50 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-09 04:50 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.71 |
| 11-09 04:50 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 04:50 | +5 | DOGE | DOWN | 0.61 | 0.78 | 1.40 |
| 11-09 04:49 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 11-09 04:49 | +10 stop | DOGE | DOWN | 0.59 | 0.78 | 1.60 |
| 11-09 04:49 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-09 04:48 | +10 stop | HYPE | DOWN | 0.67 | 0.83 | 1.32 |
| 11-09 04:48 | +10 stop | SOL | DOWN | 0.49 | 0.61 | 0.85 |
| 11-09 04:48 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-09 04:48 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 04:48 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-09 04:48 | +5 | BNB | UP | 0.59 | open |  |
| 11-09 04:48 | +5 | NEAR | UP | 0.58 | open |  |
| 11-09 04:46 | +5 | DOGE | UP | 0.55 | 0.61 | 0.25 |
| 11-09 04:46 | +10 stop | DOGE | UP | 0.59 | 0.44 | -1.85 |
| 11-09 04:46 | +20 | DOGE | UP | 0.59 | open |  |
| 11-09 04:46 | +15 | DOGE | UP | 0.59 | open |  |
| 11-09 04:46 | +10 | DOGE | UP | 0.59 | open |  |
| 11-09 04:46 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 11-09 04:46 | +10 stop | XRP | UP | 0.56 | 0.40 | -1.95 |
| 11-09 04:46 | +20 | XRP | UP | 0.56 | open |  |
| 11-09 04:46 | +15 | XRP | UP | 0.56 | open |  |
| 11-09 04:46 | +10 | XRP | UP | 0.57 | open |  |
| 11-09 04:46 | +5 | XRP | UP | 0.58 | open |  |
| 11-09 04:46 | +10 stop | SOL | UP | 0.62 | 0.43 | -2.25 |
| 11-09 04:46 | +20 | SOL | UP | 0.62 | open |  |
| 11-09 04:46 | +15 | SOL | UP | 0.62 | open |  |
| 11-09 04:46 | +10 | SOL | UP | 0.62 | open |  |
| 11-09 04:46 | +5 | SOL | UP | 0.62 | open |  |
| 11-09 04:46 | +10 stop | BNB | UP | 0.65 | 0.40 | -2.83 |
| 11-09 04:46 | +20 | BNB | UP | 0.65 | open |  |
| 11-09 04:46 | +15 | BNB | UP | 0.65 | open |  |
| 11-09 04:46 | +10 | BNB | UP | 0.65 | open |  |
