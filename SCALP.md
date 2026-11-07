# Range-Scalp Bot

*Updated Sat Nov 07 22:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51591 | 44983 | 6608 (80) | 4 | $-14317.62 | -4.4% |
| **+10¢** | 38494 | 30787 | 7707 (106) | 4 | $-13350.08 | -5.5% |
| **+15¢** | 32231 | 23925 | 8306 (135) | 5 | $-12257.68 | -6.1% |
| **+20¢** | 28668 | 19962 | 8706 (178) | 5 | $-10821.25 | -6.0% |
| **+10¢ (15¢ stop)** | 62829 | 62726 | 103 (61) | 1 | $-23276.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 22:11 | +10 stop | BNB | UP | 0.64 | open |  |
| 11-07 22:10 | +10 stop | BNB | DOWN | 0.66 | 0.38 | -3.08 |
| 11-07 22:10 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-07 22:10 | +15 | BNB | DOWN | 0.66 | open |  |
| 11-07 22:10 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-07 22:10 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-07 22:08 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-07 22:07 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.05 |
| 11-07 22:07 | +15 | NEAR | UP | 0.54 | open |  |
| 11-07 22:07 | +10 | NEAR | UP | 0.54 | open |  |
| 11-07 22:07 | +5 | NEAR | UP | 0.54 | open |  |
| 11-07 22:06 | +10 stop | XRP | UP | 0.55 | 0.23 | -3.51 |
| 11-07 22:06 | +5 | BTC | UP | 0.66 | open |  |
| 11-07 22:05 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-07 22:05 | +10 stop | XRP | UP | 0.44 | 0.57 | 0.94 |
| 11-07 22:05 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 11-07 22:05 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-07 22:05 | +10 stop | SOL | UP | 0.52 | 0.34 | -2.14 |
| 11-07 22:04 | +10 stop | ETH | DOWN | 0.63 | 0.44 | -2.25 |
| 11-07 22:04 | +10 stop | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-07 22:04 | +5 | NEAR | UP | 0.67 | 0.76 | 0.61 |
| 11-07 22:04 | +10 stop | HYPE | DOWN | 0.65 | 0.49 | -1.94 |
| 11-07 22:04 | +15 | HYPE | DOWN | 0.65 | 0.83 | 1.54 |
| 11-07 22:04 | +10 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-07 22:04 | +5 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-07 22:03 | +10 stop | ETH | DOWN | 0.50 | 0.65 | 1.16 |
| 11-07 22:03 | +5 | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 11-07 22:03 | +10 stop | BTC | UP | 0.57 | 0.68 | 0.76 |
| 11-07 22:03 | +10 stop | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-07 22:03 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 11-07 22:03 | +10 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 11-07 22:03 | +5 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 11-07 22:03 | +10 stop | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 22:03 | +20 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 22:03 | +15 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 22:03 | +10 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 22:03 | +5 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 22:02 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 22:02 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.88 |
| 11-07 22:02 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.46 |
