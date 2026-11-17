# Range-Scalp Bot

*Updated Tue Nov 17 00:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62474 | 54505 | 7969 (117) | 3 | $-16909.05 | -4.3% |
| **+10¢** | 46663 | 37337 | 9326 (159) | 3 | $-15785.36 | -5.4% |
| **+15¢** | 39109 | 29049 | 10060 (201) | 3 | $-14344.20 | -5.8% |
| **+20¢** | 34857 | 24306 | 10551 (256) | 3 | $-12530.53 | -5.7% |
| **+10¢ (15¢ stop)** | 76043 | 75887 | 156 (92) | 0 | $-28017.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 00:27 | +10 stop | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 11-17 00:25 | +10 stop | ZEC | UP | 0.60 | 0.74 | 1.10 |
| 11-17 00:24 | +10 stop | ZEC | DOWN | 0.53 | 0.65 | 0.88 |
| 11-17 00:24 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 00:21 | +10 stop | HYPE | UP | 0.49 | 0.31 | -2.13 |
| 11-17 00:21 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 11-17 00:19 | +15 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 11-17 00:19 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 00:19 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 00:19 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-17 00:18 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-17 00:17 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 00:17 | +10 stop | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 11-17 00:17 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-17 00:17 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-17 00:17 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-17 00:17 | +20 | DOGE | DOWN | 0.71 | 0.93 | 1.96 |
| 11-17 00:17 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-17 00:17 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-17 00:17 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-17 00:17 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.86 |
| 11-17 00:17 | +20 | HYPE | DOWN | 0.58 | 0.81 | 2.01 |
| 11-17 00:17 | +15 | HYPE | DOWN | 0.58 | 0.81 | 2.01 |
| 11-17 00:17 | +10 | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-17 00:17 | +5 | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-17 00:17 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.12 |
| 11-17 00:17 | +20 | SOL | DOWN | 0.60 | 0.80 | 1.71 |
| 11-17 00:17 | +15 | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 11-17 00:17 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-17 00:17 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-17 00:16 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 00:16 | +20 | XRP | DOWN | 0.70 | 0.94 | 2.26 |
| 11-17 00:16 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-17 00:16 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 00:16 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-17 00:15 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 11-17 00:15 | +20 | NEAR | UP | 0.64 | open |  |
| 11-17 00:15 | +15 | NEAR | UP | 0.64 | open |  |
| 11-17 00:15 | +10 | NEAR | UP | 0.64 | open |  |
| 11-17 00:15 | +5 | NEAR | UP | 0.64 | open |  |
