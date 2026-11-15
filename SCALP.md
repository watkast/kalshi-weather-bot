# Range-Scalp Bot

*Updated Sun Nov 15 20:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61168 | 53375 | 7793 (114) | 1 | $-16464.32 | -4.3% |
| **+10¢** | 45687 | 36555 | 9132 (153) | 1 | $-15465.92 | -5.4% |
| **+15¢** | 38267 | 28419 | 9848 (191) | 1 | $-14105.95 | -5.9% |
| **+20¢** | 34106 | 23775 | 10331 (243) | 1 | $-12388.09 | -5.8% |
| **+10¢ (15¢ stop)** | 74442 | 74290 | 152 (90) | 1 | $-27398.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 20:09 | +10 stop | HYPE | UP | 0.67 | open |  |
| 11-15 20:09 | +5 | HYPE | UP | 0.67 | open |  |
| 11-15 20:09 | +10 stop | HYPE | DOWN | 0.39 | 0.60 | 1.76 |
| 11-15 20:09 | +5 | HYPE | DOWN | 0.39 | 0.60 | 1.76 |
| 11-15 20:07 | +10 stop | HYPE | DOWN | 0.44 | 0.56 | 0.84 |
| 11-15 20:06 | +10 stop | HYPE | UP | 0.55 | 0.37 | -2.19 |
| 11-15 20:04 | +10 stop | HYPE | DOWN | 0.64 | 0.47 | -2.05 |
| 11-15 20:04 | +20 | HYPE | DOWN | 0.65 | open |  |
| 11-15 20:04 | +15 | HYPE | DOWN | 0.65 | open |  |
| 11-15 20:04 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-15 20:04 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-15 20:01 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-15 20:01 | +20 | NEAR | DOWN | 0.70 | 0.94 | 2.28 |
| 11-15 20:01 | +15 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 11-15 20:01 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-15 20:01 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-15 19:58 | +10 stop | ETH | DOWN | 0.64 | 0.39 | -2.84 |
| 11-15 19:58 | +20 | ETH | DOWN | 0.62 | 0.98 | 3.39 |
| 11-15 19:58 | +15 | ETH | DOWN | 0.62 | 0.98 | 3.39 |
| 11-15 19:58 | +10 | ETH | DOWN | 0.62 | 0.98 | 3.39 |
| 11-15 19:58 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-15 19:58 | +10 stop | HYPE | DOWN | 0.29 | 0.64 | 3.18 |
| 11-15 19:57 | +10 stop | BTC | DOWN | 0.65 | 0.22 | -4.59 |
| 11-15 19:55 | +5 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-15 19:55 | +10 stop | HYPE | UP | 0.53 | 0.31 | -2.53 |
| 11-15 19:54 | +10 stop | BNB | DOWN | 0.62 | 0.87 | 2.25 |
| 11-15 19:54 | +10 stop | SOL | DOWN | 0.68 | 0.51 | -2.04 |
| 11-15 19:54 | +20 | SOL | DOWN | 0.67 | 0.89 | 1.93 |
| 11-15 19:54 | +15 | SOL | DOWN | 0.67 | 0.89 | 1.93 |
| 11-15 19:53 | +10 stop | BTC | UP | 0.63 | 0.37 | -2.94 |
| 11-15 19:53 | +10 stop | HYPE | UP | 0.70 | 0.53 | -2.03 |
| 11-15 19:53 | +10 stop | BNB | DOWN | 0.61 | 0.46 | -1.85 |
| 11-15 19:53 | +20 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +15 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +10 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +5 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +10 stop | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-15 19:53 | +15 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-15 19:53 | +10 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-15 19:53 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
