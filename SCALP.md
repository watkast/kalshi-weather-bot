# Range-Scalp Bot

*Updated Wed Nov 18 14:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64001 | 55815 | 8186 (124) | 1 | $-17483.33 | -4.3% |
| **+10¢** | 47812 | 38234 | 9578 (165) | 1 | $-16375.63 | -5.4% |
| **+15¢** | 40090 | 29765 | 10325 (210) | 1 | $-14826.13 | -5.9% |
| **+20¢** | 35702 | 24863 | 10839 (265) | 1 | $-13133.33 | -5.9% |
| **+10¢ (15¢ stop)** | 77855 | 77691 | 164 (98) | 1 | $-28581.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 14:00 | +10 stop | DOGE | DOWN | 0.50 | open |  |
| 11-18 14:00 | +20 | DOGE | DOWN | 0.50 | open |  |
| 11-18 14:00 | +15 | DOGE | DOWN | 0.50 | open |  |
| 11-18 14:00 | +10 | DOGE | DOWN | 0.50 | open |  |
| 11-18 14:00 | +5 | DOGE | DOWN | 0.50 | open |  |
| 11-18 13:55 | +10 stop | XRP | DOWN | 0.54 | 0.85 | 2.83 |
| 11-18 13:55 | +10 stop | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 11-18 13:54 | +15 | ETH | DOWN | 0.69 | 0.88 | 1.67 |
| 11-18 13:54 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 11-18 13:54 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 13:54 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 13:54 | +10 stop | SOL | DOWN | 0.47 | 0.59 | 0.85 |
| 11-18 13:54 | +10 stop | XRP | UP | 0.63 | 0.44 | -2.25 |
| 11-18 13:53 | +10 stop | DOGE | DOWN | 0.69 | 0.51 | -2.13 |
| 11-18 13:53 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-18 13:53 | +10 stop | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 11-18 13:52 | +10 stop | ETH | DOWN | 0.70 | 0.55 | -1.83 |
| 11-18 13:52 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-18 13:52 | +5 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-18 13:52 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-18 13:52 | +10 | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-18 13:52 | +5 | BTC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-18 13:51 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-18 13:51 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 11-18 13:51 | +15 | XRP | UP | 0.69 | no | -7.05 |
| 11-18 13:51 | +10 | XRP | UP | 0.69 | no | -7.05 |
| 11-18 13:51 | +5 | XRP | UP | 0.69 | no | -7.05 |
| 11-18 13:51 | +5 | DOGE | UP | 0.65 | no | -6.66 |
| 11-18 13:51 | +10 stop | SOL | UP | 0.67 | 0.44 | -2.64 |
| 11-18 13:51 | +10 | SOL | UP | 0.67 | no | -6.86 |
| 11-18 13:51 | +5 | SOL | UP | 0.67 | no | -6.86 |
| 11-18 13:49 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-18 13:49 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-18 13:49 | +5 | SOL | UP | 0.58 | 0.67 | 0.56 |
| 11-18 13:49 | +10 stop | BTC | UP | 0.61 | 0.36 | -2.84 |
| 11-18 13:49 | +10 stop | ETH | UP | 0.60 | 0.45 | -1.85 |
| 11-18 13:48 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 11-18 13:48 | +20 | SOL | UP | 0.54 | no | -5.58 |
| 11-18 13:48 | +15 | SOL | UP | 0.54 | no | -5.58 |
| 11-18 13:48 | +10 | SOL | UP | 0.54 | 0.67 | 0.96 |
