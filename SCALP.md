# Range-Scalp Bot

*Updated Wed Nov 18 13:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63978 | 55797 | 8181 (124) | 2 | $-17461.32 | -4.3% |
| **+10¢** | 47795 | 38222 | 9573 (165) | 2 | $-16355.61 | -5.4% |
| **+15¢** | 40075 | 29755 | 10320 (210) | 3 | $-14811.20 | -5.9% |
| **+20¢** | 35688 | 24856 | 10832 (265) | 4 | $-13104.77 | -5.9% |
| **+10¢ (15¢ stop)** | 77828 | 77664 | 164 (98) | 1 | $-28576.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 13:39 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 11-18 13:39 | +10 stop | ETH | DOWN | 0.56 | 0.39 | -2.05 |
| 11-18 13:39 | +10 stop | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 11-18 13:39 | +10 | ZEC | UP | 0.63 | 0.77 | 1.10 |
| 11-18 13:39 | +5 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 11-18 13:39 | +10 stop | NEAR | UP | 0.66 | 0.89 | 2.10 |
| 11-18 13:39 | +15 | NEAR | UP | 0.66 | 0.89 | 2.10 |
| 11-18 13:39 | +10 | NEAR | UP | 0.66 | 0.89 | 2.10 |
| 11-18 13:39 | +5 | NEAR | UP | 0.65 | 0.70 | 0.22 |
| 11-18 13:38 | +10 stop | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-18 13:38 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-18 13:38 | +5 | ETH | UP | 0.67 | open |  |
| 11-18 13:38 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-18 13:38 | +15 | BTC | UP | 0.66 | open |  |
| 11-18 13:38 | +10 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-18 13:38 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-18 13:36 | +10 stop | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 11-18 13:36 | +20 | NEAR | UP | 0.64 | 0.89 | 2.26 |
| 11-18 13:36 | +15 | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 11-18 13:36 | +10 | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 11-18 13:36 | +5 | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 11-18 13:36 | +10 stop | ETH | DOWN | 0.56 | 0.33 | -2.64 |
| 11-18 13:36 | +10 stop | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-18 13:36 | +20 | ZEC | UP | 0.61 | open |  |
| 11-18 13:36 | +15 | ZEC | UP | 0.61 | 0.77 | 1.30 |
| 11-18 13:36 | +10 | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-18 13:36 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 11-18 13:35 | +10 stop | HYPE | DOWN | 0.70 | 0.52 | -2.11 |
| 11-18 13:34 | +10 stop | ETH | UP | 0.59 | 0.44 | -1.85 |
| 11-18 13:34 | +20 | ETH | UP | 0.61 | open |  |
| 11-18 13:34 | +15 | ETH | UP | 0.60 | open |  |
| 11-18 13:34 | +10 | ETH | UP | 0.59 | open |  |
| 11-18 13:34 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 11-18 13:32 | +10 stop | HYPE | UP | 0.63 | 0.48 | -1.85 |
| 11-18 13:32 | +20 | HYPE | UP | 0.63 | open |  |
| 11-18 13:32 | +15 | HYPE | UP | 0.63 | open |  |
| 11-18 13:32 | +10 | HYPE | UP | 0.64 | open |  |
| 11-18 13:32 | +5 | HYPE | UP | 0.64 | open |  |
| 11-18 13:31 | +10 stop | DOGE | UP | 0.61 | 0.75 | 1.09 |
| 11-18 13:31 | +20 | DOGE | UP | 0.61 | 0.81 | 1.72 |
