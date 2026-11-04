# Range-Scalp Bot

*Updated Wed Nov 04 22:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47640 | 41480 | 6160 (73) | 1 | $-13754.38 | -4.6% |
| **+10¢** | 35601 | 28457 | 7144 (98) | 1 | $-12554.43 | -5.6% |
| **+15¢** | 29829 | 22135 | 7694 (126) | 1 | $-11499.28 | -6.1% |
| **+20¢** | 26508 | 18449 | 8059 (166) | 1 | $-10142.17 | -6.1% |
| **+10¢ (15¢ stop)** | 58080 | 57987 | 93 (56) | 0 | $-21607.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 22:53 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-04 22:53 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-04 22:53 | +10 stop | HYPE | DOWN | 0.65 | 0.42 | -2.65 |
| 11-04 22:52 | +10 | DOGE | UP | 0.61 | 0.77 | 1.30 |
| 11-04 22:51 | +10 stop | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 11-04 22:50 | +10 stop | HYPE | DOWN | 0.69 | 0.48 | -2.43 |
| 11-04 22:50 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-04 22:49 | +10 stop | DOGE | UP | 0.60 | 0.42 | -2.15 |
| 11-04 22:49 | +5 | DOGE | UP | 0.60 | 0.67 | 0.37 |
| 11-04 22:49 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-04 22:49 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 11-04 22:49 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-04 22:49 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-04 22:49 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-04 22:49 | +10 stop | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 11-04 22:49 | +15 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 11-04 22:49 | +10 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 11-04 22:49 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 11-04 22:48 | +10 stop | SOL | UP | 0.68 | 0.52 | -1.94 |
| 11-04 22:48 | +10 stop | HYPE | UP | 0.56 | 0.40 | -1.95 |
| 11-04 22:48 | +10 stop | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 11-04 22:48 | +10 | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 11-04 22:48 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-04 22:48 | +5 | BTC | DOWN | 0.53 | 0.60 | 0.35 |
| 11-04 22:47 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 11-04 22:47 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 22:47 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 11-04 22:47 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-04 22:47 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-04 22:47 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-04 22:47 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-04 22:47 | +10 stop | BNB | DOWN | 0.56 | 0.41 | -1.85 |
| 11-04 22:47 | +20 | BNB | DOWN | 0.56 | 0.81 | 2.21 |
| 11-04 22:47 | +15 | BNB | DOWN | 0.56 | 0.81 | 2.21 |
| 11-04 22:47 | +10 | BNB | DOWN | 0.56 | 0.81 | 2.21 |
| 11-04 22:47 | +5 | BNB | DOWN | 0.56 | 0.64 | 0.45 |
| 11-04 22:46 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.85 |
| 11-04 22:46 | +20 | HYPE | UP | 0.64 | 0.86 | 1.94 |
| 11-04 22:46 | +15 | HYPE | UP | 0.64 | 0.82 | 1.52 |
| 11-04 22:46 | +10 | HYPE | UP | 0.64 | 0.82 | 1.52 |
