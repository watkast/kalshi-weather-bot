# Range-Scalp Bot

*Updated Sat Oct 10 17:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10637 | 9169 | 1468 (22) | 6 | $-3638.32 | -5.4% |
| **+10¢** | 8057 | 6348 | 1709 (36) | 6 | $-3456.04 | -6.8% |
| **+15¢** | 6798 | 4989 | 1809 (52) | 7 | $-2918.17 | -6.8% |
| **+20¢** | 6044 | 4158 | 1886 (66) | 7 | $-2491.21 | -6.6% |
| **+10¢ (15¢ stop)** | 13083 | 13042 | 41 (25) | 1 | $-5187.88 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 17:28 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-10 17:28 | +10 stop | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-10 17:28 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-10 17:28 | +10 | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-10 17:28 | +5 | BTC | DOWN | 0.54 | 0.63 | 0.55 |
| 10-10 17:27 | +10 stop | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-10 17:27 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 10-10 17:27 | +10 stop | BNB | DOWN | 0.55 | open |  |
| 10-10 17:27 | +10 stop | BNB | DOWN | 0.71 | 0.48 | -2.63 |
| 10-10 17:27 | +10 stop | ETH | UP | 0.34 | 0.62 | 2.47 |
| 10-10 17:27 | +5 | ETH | UP | 0.30 | 0.62 | 2.88 |
| 10-10 17:25 | +10 stop | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-10 17:24 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-10 17:24 | +20 | ZEC | DOWN | 0.71 | 0.96 | 2.30 |
| 10-10 17:24 | +10 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-10 17:24 | +5 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-10 17:23 | +10 stop | BTC | DOWN | 0.70 | 0.50 | -2.33 |
| 10-10 17:23 | +15 | BTC | DOWN | 0.70 | open |  |
| 10-10 17:23 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-10 17:23 | +5 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 17:23 | +10 stop | ETH | DOWN | 0.64 | 0.38 | -2.94 |
| 10-10 17:23 | +20 | ETH | DOWN | 0.64 | open |  |
| 10-10 17:23 | +15 | ETH | DOWN | 0.64 | open |  |
| 10-10 17:23 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-10 17:23 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 10-10 17:23 | +10 stop | BNB | UP | 0.61 | 0.44 | -2.05 |
| 10-10 17:23 | +10 stop | XRP | DOWN | 0.56 | 0.31 | -2.84 |
| 10-10 17:23 | +5 | XRP | DOWN | 0.56 | open |  |
| 10-10 17:23 | +10 stop | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 10-10 17:22 | +10 stop | XRP | DOWN | 0.60 | 0.73 | 0.99 |
| 10-10 17:22 | +10 stop | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 10-10 17:22 | +10 | ETH | DOWN | 0.58 | 0.76 | 1.49 |
| 10-10 17:22 | +5 | ETH | DOWN | 0.58 | 0.65 | 0.36 |
| 10-10 17:19 | +15 | ZEC | DOWN | 0.66 | 0.85 | 1.67 |
| 10-10 17:19 | +10 | ZEC | DOWN | 0.66 | 0.80 | 1.14 |
| 10-10 17:19 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.21 |
| 10-10 17:19 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 10-10 17:19 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 10-10 17:19 | +10 stop | HYPE | UP | 0.53 | 0.65 | 0.82 |
| 10-10 17:19 | +10 stop | BTC | DOWN | 0.58 | 0.42 | -1.96 |
